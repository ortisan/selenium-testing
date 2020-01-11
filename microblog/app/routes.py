from flask import render_template
from app import app
from app.forms import PostForm

user = {'username': 'Marcelo'}

posts = [
        {
            'author': user,
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': user,
            'body': 'The Avengers movie was so cool!'
        }
    ]

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        body = form.body.data
        posts.append({'author': user, 'body': body})
    return render_template('index.html', title='Home', form=form, user=user, posts=posts)