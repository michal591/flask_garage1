"""
דף בית
ADD
LOGIN
LOG OUT
EDIT
SEARCH
DELETE
CART
"""

from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "your_secret_key"

car1 = {
    "id": 1,
    "number": "1234567",
    "problem": ["engine", "filter"],
    "urgent": True,
    "image": "https://www.cars.com/i/large/in/v2/stock_photos/9ba1b9ad-de13-484c-92cf-fbfc28e6432f/02c3ba77-60fd-462c-b09a-0e0eedfcc85c.png",
}
car2 = {
    "id": 2,
    "number": "2345678",
    "problem": ["breaks", "filter"],
    "urgent": True,
    "image": "https://www.motortrend.com/uploads/sites/10/2023/11/2024-audi-a5-sportback-premium-plus-4wd-5door-hatchback-angular-front.png",
}
car3 = {
    "id": 3,
    "number": "3456789",
    "problem": ["engine", "gear"],
    "urgent": True,
    "image": "https://d2ivfcfbdvj3sm.cloudfront.net/7fc965ab77efe6e0fa62e4ca1ea7673bb65848560e1e3d8e88cb10/stills_0640_png/MY2023/52975/52975_st0640_116.png",
}
cars = [car1, car2, car3]


@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        return f'Logged in as {username} <br><a href="/logout">Logout</a>'
        
    return 'You are not logged in <br><a href="/login">Login</a>'


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
