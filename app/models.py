from flask.ext.wtf import Form
from datetime import date
from wtforms import StringField, SelectField, SubmitField
from flask.ext.admin.form.widgets import DatePickerWidget
from wtforms.fields.html5 import DateField, EmailField
from wtforms.validators import Required
from app.lookUp import characters, city_dict

class NameForm(Form):
	firstName = StringField("First name", validators=[Required()])
	lastName = StringField("Last name", validators=[Required()])
	userName = StringField("Enter a Username", validators=[Required()])
	birthdate = DateField('Birthdate', format="%m/%d/%Y", widget=DatePickerWidget())
	email = EmailField("Email")
	character = SelectField("Who's your favorite character?", coerce=str, 
		choices = [(i,i) for n,i in enumerate(sorted(characters))])
	city = SelectField("Where are you from?", coerce=str,
		choices=[(i,i) for i in city_dict.keys()],
		validators=[Required()], 
		) #Requiring a region.
	submit = SubmitField("Submit")

