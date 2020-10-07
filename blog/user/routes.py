from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, url_for, flash, redirect, request, Blueprint
from blog import db, bcrypt 
from blog.models import User, Post
from blog.user.utiles import send_reset_password_email, save_image
from blog.user.forms import RegisterationForm, LoginForm, UpdateAccountForm, ResetRequestForm, ResetPasswordForm

user = Blueprint('user', __name__)


@user.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account Successfully Created, Now You Can Login!', 'success')
        return redirect(url_for('user.login'))
    return render_template('signup.html', title="Sign Up", form=form)

@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f"You have successfully logged with {form.email.data} email!", 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f"Login Faild. Please provide correct username and password!", 'danger')
    return render_template('login.html', title="Login", form=form)

@user.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('user.login'))

@user.route('/account', methods=['GET', 'POST'])
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
        return redirect(url_for('user.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_image = url_for('static', filename='profiles/' + current_user.image_file)
    return render_template('account.html', title="Account", profile_image=profile_image, form=form)

@user.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=3)
    return render_template('user_posts.html', title='User Posts', posts=posts, user=user)

@user.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
       return redirect('home.html')
    form = ResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_password_email(user)
        flash('An reset link has been sent to your email, please open your email and reset your password.', 'info')
    return render_template('reset_request.html', title="Reset Password", form=form)

@user.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('user.request_password'))
    user = User.check_reset_token(token)
    if not user:
        flash('This is not a valid token!', 'Warning')
        return redirect(url_for('user.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated!. You can login now.', 'success')
        return redirect(url_for('user.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)