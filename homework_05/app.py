"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, Blueprint, render_template

homework_app = Blueprint("homework_app", __name__)

app = Flask(__name__)

@homework_app.get("/", endpoint="home_page_endpoint")
def home_page():
    return render_template("index.html")

@homework_app.get("/about/", endpoint="about_page_endpoint")
def about_page():
    return render_template("about.html")

app.register_blueprint(homework_app, url_prefix="")





