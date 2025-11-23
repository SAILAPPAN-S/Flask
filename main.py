from flask import Flask,Blueprint,render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello World!"

@main.route('/profile')
def profile():
    return "Profile of the user" 