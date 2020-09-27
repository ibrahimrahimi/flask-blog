from flask import render_template, url_for, flash, redirect
from blog import app, db, bcrypt
from blog.models import User, Post
from blog.forms import RegisterationForm, LoginForm
import os

posts = [
    {
        'title': 'First Post',
        'author': 'Ahmad',
        'posted_date': 'September 22, 2020',
        'content': 'This is content for first post.'
    },
    {
        'title': 'Second Post',
        'author': 'Rahim',
        'posted_date': 'September 23, 2020',
        'content': 'This is some test text content for second post. The purpose is to see these sentences as test in view.'
    },

]

db.create_all()
db.session.commit()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterationForm()
    if form.validate_on_submit():
        basedir = os.path.abspath(os.path.dirname(__file__))
        print('basedir::::::', basedir)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account Successfully Created, Now You Can Login!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title="Sign Up", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'irahimi@netlinks.af' and form.password.data == 'testpass':
            flash(f"You have successfully logged with {form.email.data} email!", 'success')
            return redirect(url_for('home'))
        else:
            flash(f"Login Faild. Please provide correct username and password!", 'danger')
    return render_template('login.html', title="Login", form=form)

@app.route('/contact')
def contact():
   return render_template('contact.html', title='Contact')

@app.route('/service')
def service():
   return render_template('service.html', title='Services')