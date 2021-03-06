from flask import Flask


def create_app():
    app = Flask(__name__)

    from .views import views
    #from .auth import auth


    app.register_blueprint(views, urlprefix='/')
    #app.register_blueprint(auth, urlprefix='/')

    return app
