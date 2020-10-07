from flask import render_template, Blueprint, request
from blog import db
from blog.models import Post

main = Blueprint('main', __name__)

db.create_all()
db.session.commit()

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html', title="About")


@main.route('/contact')
def contact():
   return render_template('contact.html', title='Contact')

@main.route('/service')
def service():
   return render_template('service.html', title='Services')
