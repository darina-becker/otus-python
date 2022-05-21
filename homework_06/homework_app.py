from turtle import title
from requests import post
from models import User, Post
from database import db

from flask import Blueprint, render_template, request, redirect, url_for
from forms import UsersAddForm, PostsAddForm
from sqlalchemy.exc import DatabaseError
from werkzeug.exceptions import InternalServerError



homework_app = Blueprint("homework_app", __name__)

@homework_app.get("/", endpoint="home_page_endpoint")
def home_page():
    return render_template("index.html")

@homework_app.get("/users", endpoint="users_page_endpoint")
def home_page():
    users: list[User] = User.query.all()
    return render_template("users.html", users=users)

@homework_app.get("/posts", endpoint="posts_page_endpoint")
def home_page():
    posts: list[Post] = Post.query.all()
    return render_template("posts.html", posts=posts)

@homework_app.route("/users/add", methods=["GET", "POST"], endpoint="users_add_endpoint")
def users_add():

    form = UsersAddForm()
    if request.method == "GET":
        return render_template("add_users.html", form=form)

    user_name = form.data["name"]

    user = User(name=user_name)
    db.session.add(user)

    try:
        db.session.commit()
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError(f"could not save user, unexpected error")

    return redirect(url_for("homework_app.users_page_endpoint"))

@homework_app.route("/posts/add", methods=["GET", "POST"], endpoint="posts_add_endpoint")
def posts_add():

    form = PostsAddForm()
    if request.method == "GET":
        return render_template("add_posts.html", form=form)

    post_title = form.data["name"]

    post = Post(title=post_title)
    db.session.add(post)

    try:
        db.session.commit()
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError(f"could not save post, unexpected error")

    return redirect(url_for("homework_app.posts_page_endpoint"))