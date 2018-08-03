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
from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm #When in package, import with 'pkg_name.file'
from flaskblog.models import User, Post

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
