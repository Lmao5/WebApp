from wtforms import Form, StringField, SelectField, TextAreaField, validators
from wtforms.fields.html5 import EmailField

class FeedbackForm(Form):
 FirstName = StringField('First Name', [validators.Length(min=1,max=150), validators.DataRequired()])
 SecondName = StringField('Second Name', [validators.Length(min=1, max=150), validators.DataRequired()])
 email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
 feedback = TextAreaField('message', [validators.DataRequired])
