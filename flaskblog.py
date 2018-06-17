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
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
# All Flask app must create an app instance like this:
app = Flask(__name__)
app.config['SECRET_KEY'] =' 67aGHYDS8c7S8CGcaydw878csa7887bac'

posts = [
    {
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

# Invoke this one with http://127.0.0.1:5000
@app.route('/')
@app.route('/home')
def Index():
   return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = "About")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title = "Register", form = form)

@app.route('/login')
def login():
    form = LoginForm()
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
