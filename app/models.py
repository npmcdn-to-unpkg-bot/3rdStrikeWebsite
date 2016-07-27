from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import Required
characters = ["", "Alex", "Akuma", "Chun Li", "Dudley", "Elena", "Hugo", "Ibuki", "Ken", 
"Makoto", "Necro", "Oro", "Q", "Remy", "Ryu", "Sean", "Twelve", "Urien", "Yang", "Yun"]

class NameForm(Form):
	name = StringField("What's your name?", validators=[Required()])
	nickname = StringField("What's your handle/nickname?", validators=[Required()])
	age = IntegerField("What's your age?")
	character = SelectField("Who's your favorite character?", coerce=str, 
		choices = [(i,i) for n,i in enumerate(sorted(characters))])
	region = StringField("Where are you from?", validators=[Required()])
	submit = SubmitField("Submit")