from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired()])
    name = StringField('name',
                       validators=[DataRequired(), Length(min=2, max=40)])
    title = StringField('title',
                        validators=[DataRequired(), Length(min=1, max=80)])
    submit = SubmitField('send')
