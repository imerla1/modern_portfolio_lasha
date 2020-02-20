from flask import render_template, request, Blueprint

contact = Blueprint('contact', __name__)


@contact.route("/reachme")
def reachme():
    return render_template('reachme.html', title='reachme')


@contact.route("/contactme")
def contactme():
    return render_template('contact.html', title='My Work')
