from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p> Login you self </p>"

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/sign-up')
def sign():
    return "<p> Sign Up </p>"
    
