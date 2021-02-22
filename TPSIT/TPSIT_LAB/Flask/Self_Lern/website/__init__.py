from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy



db= SQLAlchemy()
DBNAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KARNISINGHSHEKHAWAT'
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DBNAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth


    app.register_blueprint(views, urlprefix='/')
    app.register_blueprint(auth, urlprefix='/')


    return app

