from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:password@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask!'


@app.route('/custom-greeting/')
def custom_greeting(greeting='Hello'):
    greeting_value = request.args.get('greeting', greeting)
    return f'<h1>The greeting is: {greeting_value}</h1>'


@app.route('/user')
@app.route('/user/<name>')
def custom_greeting_without_query_string(name='No name'):
    return f'<h1>Hi {name}!</h1>'


@app.route('/display-float/<float:num>')
def display_float(num: float):
    return f'<h1>The float passed is {str(num)}</h1>'


@app.route('/add/<int:num1>/<int:num2>')
def add_integers(num1: int, num2: int):
    return f'<h1>{num1} + {num2} = {num1 + num2}</h1>'


@app.route('/template')
def using_template():
    return render_template('hello.html')


@app.route('/watch/<string:name>')
def top_movies(name: str):
    movie_list = ['autopsy of jane doe',
                  'neon demon',
                  'ghost in a shell',
                  'kong: skull island',
                  'john wick 2',
                  'spiderman - homecoming']

    return render_template('movies.html',
                           movies=movie_list,
                           name=name)


@app.route('/table/<string:name>')
def movies_plus(name: str):
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('table.html',
                           movies=movies_dict,
                           name=name)


@app.route('/filter')
def filter_data():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('filter.html',
                           movies=movies_dict,
                           name=None,
                           film='a christmas carol')


@app.route('/macro')
def jinja_macros():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('using_macro.html', movies=movies_dict)


class Publisher(db.Model):
    __tablename__ = 'Publisher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'Publisher ID is {self.id}, publisher name is {self.name}'


if __name__ == '__main__':
    db.create_all()  # create tables if they don't exist
    app.run(debug=True)
