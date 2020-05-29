from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '36a2d244138a60a3db8b052f714503ca'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////site.db'
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
        'author': 'Sean Davis',
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


if __name__ == '__main__':
    app.run(debug=True)

# from random_word import RandomWords
#
#
# def find_occurrence(character):
#     for index, current_letter in enumerate(word):
#         if current_letter == character:
#             yield index
#
#
# def fill_in(character):
#     for occ in find_occurrence(character):
#         guess[occ] = character
#
#
# difficulty = input("Choose your difficulty level: easy/medium/hard: ")
# if difficulty == "easy":
#     no_of_guesses = 20
# elif difficulty == "medium":
#     no_of_guesses = 12
# elif difficulty == "hard":
#     no_of_guesses = 7
#
# r = RandomWords()
#
# # Return a single random word
# word = r.get_random_word(hasDictionaryDef="true")
#
# length = len(word)
# print("Length: {}".format(length))
#
# first_letter = word[0]
# print("First letter: {}".format(first_letter))
#
# last_letter = word[length - 1]
# print("Last letter: {}".format(last_letter))
#
# # Initialise guess with first and last letter
# guess = [None] * length
# guess[0] = first_letter
# guess[len(guess) - 1] = last_letter
#
# # Fill in the guess with other occurrences of the first and last letter
# fill_in(first_letter)
# fill_in(last_letter)
#
# guesses = set()
#
# # Guessing starts
# while no_of_guesses:
#     print("------------------------------------------------------------")
#     print("Current guess: {}".format(guess))
#     print("You have {} guesses left".format(no_of_guesses))
#
#     letter = input("Your guess: ")
#     if letter in guesses:
#         print("You already tried this one!")
#         print("The letters you already tried are: {}".format(sorted(guesses)))
#     else:
#         if letter in word:
#             print("Hooray! {} was correct!".format(letter))
#             fill_in(letter)
#             print(guess)
#
#             if guess == list(word):
#                 print("Congrats! The word was {}".format(word))
#                 exit()
#
#         else:
#             no_of_guesses -= 1
#         guesses.add(letter)
#
# print("Sad. The word was: {}".format(word))
