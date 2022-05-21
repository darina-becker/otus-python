from os import getenv
from flask import Flask
from database import db

from distutils.command.config import config
from flask_migrate import Migrate
from homework_app import homework_app


app = Flask(__name__)
CONFIG_PATH = "config.{}".format(getenv("CONFIG_NAME", "DevelopmentConfig"))
# CONFIG_PATH = "config.ProductionConfig"

app.config.from_object(CONFIG_PATH)

db.init_app(app)

migrate = Migrate(app, db)


app.register_blueprint(homework_app, url_prefix="")

if __name__ == '__main__':
    app.run(host="0.0.0.0")