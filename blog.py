from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '37796a65dd2d6d4957d197aba95dedc1'

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
        flash(f'Account successfully created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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

if __name__ == '__main__':
    app.run(debug=True)