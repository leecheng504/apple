from flask import Flask
app = Flask(__name__)  # __name__代表目前執行的模組
Bootstrap(app)


@app.route("/")  # 已函示為基礎，提供附加的功能
def home():
    return render_template("introduce.html")


if __name__ == "__main__":  # 如果以主程式執行
    app.run(debug=True)  # 立即啟動伺服器
