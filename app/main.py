from flask import Flask,Blueprint,render_template

main = Blueprint('main', __name__)

@main.route('/index')
def home():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html') 