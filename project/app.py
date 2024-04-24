from flask import Flask, render_template
import random
from collections import Counter

app = Flask(__name__)

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def create_deck():
    return [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

def evaluate_hand(hand):
    ranks = [card['rank'] for card in hand]
    suits = [card['suit'] for card in hand]
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)
    is_flush = len(set(suits)) == 1
    rank_values = [ranks.index(rank) for rank in ranks]
    rank_values.sort()
    is_straight = all(rank_values[i] - rank_values[i - 1] == 1 for i in range(1, len(rank_values)))

    if is_flush and is_straight:
        return "Straight Flush"
    elif 4 in rank_counts.values():
        return "Four of a Kind"
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif 3 in rank_counts.values():
        return "Three of a Kind"
    elif list(rank_counts.values()).count(2) == 2:
        return "Two Pair"
    elif 2 in rank_counts.values():
        return "One Pair"
    else:
        return "High Card"

@app.route('/')
def poker_game():
    deck = create_deck()
    random.shuffle(deck)
    hand = deck[:5]
    hand_rank = evaluate_hand(hand)
    return render_template('index.html', hand=hand, hand_rank=hand_rank)

if __name__ == '__main__':
    app.run(debug=True)
