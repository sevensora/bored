from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import random

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def create_deck():
    return [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

def card_value(card):
    if card['rank'] in ['Jack', 'Queen', 'King']:
        return 10
    elif card['rank'] == 'Ace':
        return 11  # Initially treat Ace as 11
    else:
        return int(card['rank'])

def hand_value(hand):
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card['rank'] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def initialize_game():
    deck = create_deck()
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    session['deck'] = deck
    session['player_hand'] = player_hand
    session['dealer_hand'] = dealer_hand
    session['player_value'] = hand_value(player_hand)
    session['dealer_value'] = hand_value(dealer_hand)

@app.route('/', methods=['GET', 'POST'])
def blackjack_game():
    if 'player_hand' not in session:
        initialize_game()

    if request.method == 'POST':
        if 'hit' in request.form:
            session['player_hand'].append(session['deck'].pop())
            session['player_value'] = hand_value(session['player_hand'])
            if session['player_value'] > 21:
                message = 'Bust It! You lose.'
                session.clear()
                return render_template('end_screen.html', message=message)
            session.modified = True
        elif 'stand' in request.form:
            while session['dealer_value'] < 17:
                session['dealer_hand'].append(session['deck'].pop())
                session['dealer_value'] = hand_value(session['dealer_hand'])
            player_total = session['player_value']
            dealer_total = session['dealer_value']
            if dealer_total > 21:
                message = 'Dealer busts! You win!'
            elif player_total > dealer_total:
                message = 'Congratulations, you won!'
            elif player_total < dealer_total:
                message = 'Dealer has a better hand! You lose.'
            else:
                message = 'It\'s a draw!'
            session.clear()
            return render_template('end_screen.html', message=message)

    return render_template('index.html', player_hand=session.get('player_hand', []), dealer_hand=session.get('dealer_hand', []), player_value=session.get('player_value', 0), dealer_value=session.get('dealer_value', 0), message=None)

@app.route('/play_again', methods=['GET'])
def play_again():
    session.clear()  # Reset the game state
    return redirect(url_for('blackjack_game'))

if __name__ == '__main__':
    app.run(debug=True)
