from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello 這是我們專題的網頁"


@app.route("/test")
def test():
    return "hi"


if __name__ == "__main__":
    app.run()
