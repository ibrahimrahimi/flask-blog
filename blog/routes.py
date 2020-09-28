import os
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from blog import app, db, bcrypt
from blog.models import User, Post
from blog.forms import RegisterationForm, LoginForm

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account Successfully Created, Now You Can Login!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title="Sign Up", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f"You have successfully logged with {form.email.data} email!", 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f"Login Faild. Please provide correct username and password!", 'danger')
    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('login'))

@app.route('/account')
@login_required
def account():
    profile_image = url_for('static', filename='profiles/' + current_user.image_file)
    return render_template('account.html', title="Account", profile_image=profile_image)

@app.route('/contact')
def contact():
   return render_template('contact.html', title='Contact')

@app.route('/service')
def service():
   return render_template('service.html', title='Services')