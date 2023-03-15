from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()


def create_app():
    app = Flask(__name__)
    mysql = MySQL()
    app.config['SECRET_KEY'] = "supernessecary"
    app.config['MYSQL_DATABASE_USER'] = '19990730'
    app.config['MYSQL_DATABASE_PASSWORD'] = '19990730'
    app.config['MYSQL_DATABASE_DB'] = 'db19990730'
    app.config['MYSQL_DATABASE_HOST'] = 'utbweb.its.ltu.se'
    mysql.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app