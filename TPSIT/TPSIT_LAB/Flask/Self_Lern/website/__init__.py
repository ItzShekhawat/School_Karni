from flask import Flask, app

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KARNISINGHSHEKHAWAT'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, urlprefix='/')
    app.register_blueprint(auth, urlprefix='/')

    return app

