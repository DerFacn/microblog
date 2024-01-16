from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from app.models import Base, Post
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///app.db', echo=True)
session = scoped_session(sessionmaker(autoflush=False, bind=engine))
Base.metadata.create_all(bind=engine)
Base.session = session.query_property()


@app.route('/')
def index():
    posts = session.query(Post).all()
    return render_template('index.html', posts=posts)


@app.route('/', methods=['POST'])
def create_post():
    title = request.form.get('title', None)
    body = request.form.get('body', None)
    if not title or not body:
        return 'Title and body required!'
    new_post = Post(title=title, body=body)
    try:
        session.add(new_post)
        session.commit()
    except IntegrityError:
        return 'Your post is very big!!!!'
    return redirect(url_for('index'))
