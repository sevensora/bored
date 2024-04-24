import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd


# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd
app.jinja_env.globals.update(usd=usd)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    transactions_db = db.execute(
        "SELECT symbol, SUM(shares) AS shares, price FROM transactions WHERE user_id = ?", user_id)
    cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash_db[0]["cash"]

    return render_template("index.html", database=transactions_db, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper().strip()
        if not symbol:
            return apology("Please provide a stock symbol.")

        try:
            shares = float(request.form.get("shares"))

            if shares != int(shares) or shares <= 0:
                return apology("Number of shares must be a positive integer.")
            shares = int(shares)
        except ValueError:
            return apology("Number of shares must be a numeric value.")

        quote = lookup(symbol)
        if quote is None:
            return apology("Stock symbol not found. Please enter a valid symbol.")

        price = quote['price']
        total_cost = shares * price
        user_id = session["user_id"]
        user_cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                               user_id=user_id)[0]["cash"]

        if user_cash < total_cost:
            return apology("Insufficient funds to complete purchase.")

        db.execute("UPDATE users SET cash = cash - :total_cost WHERE id = :user_id",
                   total_cost=total_cost, user_id=user_id)

        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, type) VALUES (:user_id, :symbol, :shares, :price, 'buy')",
                   user_id=user_id, symbol=symbol, shares=shares, price=price)

        flash(f"Successfully bought {shares} shares of {symbol} at {
              usd(price)} each, total cost {usd(total_cost)}.")
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = :user_id ORDER BY timestamp DESC", user_id=session["user_id"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)

        if not quote:
            return apology("Symbol not valid", 400)
        return render_template("quote.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("All fields must be filled", 400)

        if password != confirmation:
            return apology("Passwords do not match", 400)

        user_check = db.execute("SELECT * FROM users WHERE username = ?", username)
        if user_check:
            return apology("Username already exists", 400)

        hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

        flash("Registered successfully! You can now log in.")
        return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        user_id = session["user_id"]
        symbols_user = db.execute(
            "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :id GROUP BY symbol HAVING total_shares > 0", id=user_id)
        return render_template("sell.html", symbols=[row["symbol"] for row in symbols_user])


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Allow user to change password."""
    if request.method == "POST":
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        if not current_password or not new_password or not confirmation:
            return apology("Must provide all password fields", 403)

        user_id = session["user_id"]
        user = db.execute("SELECT hash FROM users WHERE id = :user_id", user_id=user_id)

        if not check_password_hash(user[0]['hash'], current_password):
            return apology("Invalid current password", 403)

        if new_password != confirmation:
            return apology("New passwords do not match", 403)

        new_password_hash = generate_password_hash(new_password)
        db.execute("UPDATE users SET hash = :new_hash WHERE id = :user_id",
                   new_hash=new_password_hash, user_id=user_id)

        flash("Your password has been changed successfully.")
        return redirect("/")
    else:
        return render_template("change_password.html")
