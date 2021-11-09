from flask import Flask, request, render_template

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


@app.route("/template")
def using_template():
    return render_template("hello.html")


@app.route("/watch/<string:name>")
def top_movies(name: str):
    movie_list = [
        "autopsy of jane doe",
        "neon demon",
        "ghost in a shell",
        "kong: skull island",
        "john wick 2",
        "spiderman - homecoming"
    ]

    return render_template("movies.html",
                           movies=movie_list,
                           name=name)


if __name__ == "__main__":
    app.run(debug=True)
