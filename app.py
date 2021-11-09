from flask import Flask, request

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def hello_flask():
    return "Hello Flask!"


@app.route("/custom-greeting/")
def custom_greeting(greeting="Hello"):
    greeting_value = request.args.get("greeting", greeting)
    return f"<h1>The greeting is: {greeting_value}</h1>"


@app.route("/user")
@app.route("/user/<name>")
def custom_greeting_without_query_string(name="No name"):
    return f"<h1>Hi {name}!</h1>"


@app.route("/display-float/<float:num>")
def display_float(num: float):
    return f"<h1>The float passed is {str(num)}</h1>"


@app.route("/add/<int:num1>/<int:num2>")
def add_integers(num1: int, num2: int):
    return f"<h1>{num1} + {num2} = {num1 + num2}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
