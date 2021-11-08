from flask import Flask, request

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def hello_flask():
    return "Hello Flask!"


@app.route("/custom-greeting/")
def custom_greeting():
    greeting_value = request.args.get("greeting")
    return f"<h1>The greeting is: {greeting_value} </h1>"


if __name__ == '__main__':
    app.run(debug=True)
