from flask import render_template, request, Blueprint
from app.contanct.forms import ContactForm
from app.contanct.utils import send_mail

contact = Blueprint('contact', __name__)


@contact.route("/reachme")
def reachme():
    return render_template('reachme.html', title='reachme')


@contact.route("/contactme", methods=['GET', 'POST'])
def contactme():
    form = ContactForm()
    if form.validate_on_submit():

        name = form.name.data
        title = form.title.data
        content = form.content.data
        send_mail(title=title, sender_name=name, body=content)
        return str(name)
    return render_template('contact.html', title='My Work', form=form)
