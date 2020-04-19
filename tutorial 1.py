from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return f"Welcome to this home page <h1>Hello Keep Safe this is Billy Gareth<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}! How're you doing?....."

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()