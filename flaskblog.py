# Simple example
#
# This example (simple.py) shows the basic structure of a Flask program.
#
# To run this app do:
#
#    1. Start your app from the command line:
#
#       terminal> python simple.py
#
#    2. Invoke it on your web browser by:
#       http://127.0.0.1:5000
#       or
#       http://localhost:5000
#
#    3. ctl-C on terminal to kill the server program when you are done.
# Import Flask so that we can create an app instance
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm
# All Flask app must create an app instance like this:
app = Flask(__name__)
app.config['SECRET_KEY'] =' 67aGHYDS8c7S8CGcaydw878csa7887bac' #setting secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #importing sqldatabase

db = SQLAlchemy(app) #database structure as models

class User(db.Model): #User data base class
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(20), unique = True, nullable = False)
    image_file = db.Column(db.String(20), unique = True, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model): #post data base class
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(20), unique = False, nullable = False)
    title = db.Column(db.String(120), unique = False, nullable = False)
    content = db.Column(db.Text, nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(post):
        return f"Post('{self.author}', '{self.title}', '{self.content}', '{self.date_posted}')"

posts = [
    {
        #dummy data
        'author' : 'Bradley Justice',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 22, 2018'
    }
]

# Invoke this with http://127.0.0.1:5000
@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = "About")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = "Register", form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login(): #login forms, passing and receiving flash messages for logins
    form = LoginForm()
    if form.validate_on_submit(): #if login successful return to home page
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = "Login", form = form)

# Invoke this one with http://127.0.0.1:5000/hello
@app.route('/hello')
def hello():
   f = open ("testfile.txt", "w+")
   for i in range (10):
      f.write("This is line %d\r\n" % (i + 1))
   f.close()
   return '<h1>Hello World this is me</h1>'


# Now, run the app as a server in debug mode
if __name__ == '__main__':
    app.run(debug=True)
