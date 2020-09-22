from flask import Flask, render_template, url_for
from forms import RegisterationForm


app = Flask(__name__)

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

@app.route('/signup')
def signup():
    form = RegisterationForm()
    return render_template('signup.html', title="Sign Up", form=form)

if __name__ == '__main__':
    app.run(debug=True)