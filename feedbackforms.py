from wtforms import *
from wtforms.fields.html5 import *

class FeedbackForm(Form):
 fullName = StringField('Full Name', [validators.Length(min=1,max=150), validators.DataRequired()])
 email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
 feedback = TextAreaField('message', [validators.DataRequired()])

class CheckoutForm(Form):
 email = EmailField('Email',[validators.DataRequired(), validators.Email()])
 phone = IntegerField('Phone number')
 fullName = StringField('Full name', [validators.DataRequired()])
 optin = BooleanField('Opt in to our mailing list')
 address = StringField('Address', [validators.DataRequired()])
 city = StringField('City', [validators.DataRequired()])
 apartment = StringField('Apartment', [validators.DataRequired()])
 postalcode = StringField('Postal Code', [validators.DataRequired()])


