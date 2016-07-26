from run import db
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import Required
characters = ["", "Alex", "Akuma", "Chun Li", "Dudley", "Elena", "Hugo", "Ibuki", "Ken", 
"Makoto", "Necro", "Oro", "Q", "Remy", "Ryu", "Sean", "Twelve", "Urien", "Yang", "Yun"]


class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	
	def __repr__(self):
		return '<User {}>'.format(self.nickname)


class NameForm(Form):
	name = StringField("What's your name?", validators=[Required()])
	age = IntegerField("What's your age?")
	character = SelectField("Who's your favorite character?", coerce=str, 
		choices = [(i,i) for n,i in enumerate(sorted(characters))])
	region = StringField("Where are you from?")
	submit = SubmitField("Submit")