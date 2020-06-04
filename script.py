from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging
from random_word import RandomWords
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = '36a2d244138a60a3db8b052f714503ca'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Volumes/unix/workplace/Game/hangman/site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Natalia Gutanu',
        'title': 'Blog Post 1',
        'content': 'First blog post content',
        'date_posted': 'April 20th, 2019'
    },
    {
        'author': 'Sean DeVis',
        'title': 'Blog Post 2',
        'content': 'Second blog post content',
        'date_posted': 'April 21st, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About MEEEEE')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success', )
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/new_game')
def new_game():
    return render_template('new_game.html', title='New Hangman Game')


@app.route('/new_game', methods=['GET'])
def get_level():
    level = request.form['level']
    return level


def get_no_of_guesses():
    level = get_level()
    if level == 'easy':
        no_of_guesses = 20
    elif level == 'medium':
        no_of_guesses = 10
    else:
        no_of_guesses = 7

    return no_of_guesses


@app.route('/new_game', methods=['POST'])
def post_level():
    return redirect(url_for('game', guesses=get_no_of_guesses(), level=get_level()))


class Word:
    r = RandomWords()
    WORD = r.get_random_word(hasDictionaryDef="true")


@app.route('/game')
def game():
    word = Word().WORD
    level = request.args['level']
    return render_template('game.html', title='Hangman', word=word, level=level)


@app.route('/game', methods=['GET'])
def game_get_text():
    text = request.form['text']
    return text


guessed_letters = set()
guessed_letters.add(Word.WORD[0])
guessed_letters.add(Word.WORD[len(Word.WORD) - 1])
false_guesses = set()


@app.route('/game', methods=['GET'])
def get_guesses():
    initial_guesses = int(request.args['guesses'])

    return initial_guesses - len(false_guesses)


@app.route('/game', methods=['POST'])
def game_post():
    new_guess = game_get_text()

    level = request.args['level']
    guessed = "False"

    word = Word().WORD
    target_letters = set(word)

    init_guess = init_guess_list(word, guessed_letters)
    current_guess_text_final = get_current_guess_text(init_guess)

    if new_guess in guessed_letters:
        print("You already tried this one!")
    else:
        if new_guess in word:
                guessed = "True"
                guessed_letters.add(new_guess)
                new_guess_list = fill_in(init_guess, new_guess, word)
                current_guess_text_final = get_current_guess_text(new_guess_list)
        else:
            if new_guess in false_guesses:
                "You already tried this one and it's still wrong!"
            elif new_guess not in word:
                    false_guesses.add(new_guess)

    if target_letters == guessed_letters:
        return render_template('home.html', success='Sucess!')

    if get_guesses() == 0:
        return render_template('home.html', success='Fail!')

    guesses = get_guesses()

    return render_template('game.html', title='Hangman', value=guessed, word=word, guesses=guesses, level=level,
                           current_guess=str(current_guess_text_final))


def find_occurrence(character, word):
    for index, current_letter in enumerate(word):
        if current_letter == character:
            yield index


def fill_in(guess, character, word):
    for occ in find_occurrence(character, word):
        guess[occ] = character

    return guess


def init_guess_list(word, guessed_letters):
    length = len(word)
    current_guess = [None] * length
    for letter in guessed_letters:
        current_guess = fill_in(current_guess, letter, word)

    return current_guess


def get_current_guess_text(current_guess):
    length = len(current_guess)
    current_guess_text = ['_'] * length

    for index, letter in enumerate(current_guess):
        if letter in list(string.ascii_lowercase):
            current_guess_text[index] = letter

    current_guess_text_final = ""
    for character in current_guess_text:
        current_guess_text_final += character
        current_guess_text_final += ' '

    return current_guess_text_final


if __name__ == '__main__':
    app.run(debug=True)
