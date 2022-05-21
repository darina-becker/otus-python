from flask_wtf import FlaskForm
from wtforms import StringField

class UsersAddForm(FlaskForm):
    name = StringField("User name", name="user-name")

class PostsAddForm(FlaskForm):
    name = StringField("Post title", name="post-title")