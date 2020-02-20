from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
def home():
    return render_template('index.html', title='Home Page')


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/work")
def work():
    return render_template('work.html', title='My Work')
