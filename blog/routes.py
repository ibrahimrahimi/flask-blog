import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from blog import app, db, bcrypt
from blog.models import User, Post
from blog.forms import RegisterationForm, LoginForm, UpdateAccountForm, PostForm


db.create_all()
db.session.commit()

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
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

def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, iext = os.path.splitext(form_image.filename)
    image_fn = random_hex + iext
    image_path = os.path.join(app.root_path, 'static/profiles', image_fn)
    
    output_image_size = (150, 150)
    image = Image.open(form_image)
    image.thumbnail(output_image_size)
    image.save(image_path)
    return image_fn

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.profile.data:
            profile_image = save_image(form.profile.data)
            current_user.image_file = profile_image
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated successfully!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_image = url_for('static', filename='profiles/' + current_user.image_file)
    return render_template('account.html', title="Account", profile_image=profile_image, form=form)

@app.route('/contact')
def contact():
   return render_template('contact.html', title='Contact')

@app.route('/service')
def service():
   return render_template('service.html', title='Services')

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, date_posted=datetime.now(), content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form)