from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def exercise(name):
    return render_template("index.html", content=name, var=16748)

@app.route("/py")
def loops():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()