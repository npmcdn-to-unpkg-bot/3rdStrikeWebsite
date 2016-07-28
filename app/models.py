from flask_wtf import Form
from run import db
from datetime import date
from wtforms import StringField, SelectField, SubmitField, TextField, validators
from wtforms.widgets import TextArea
from wtforms.fields.html5 import DateField, EmailField
from wtforms.validators import Required
from werkzeug.security import generate_password_hash, check_password_hash
from app.lookUp import characters, city_dict

class NameForm(Form):
	firstName = StringField("First name", validators=[Required()])
	lastName = StringField("Last name", validators=[Required()])
	userName = StringField("Enter a Username", validators=[Required()])
	password = StringField("Enter a passowrd", validators=[Required()])
	birthdate = DateField('Birthdate')
	email = EmailField("Email")
	character = SelectField("Who's your favorite character?", coerce=str, 
		choices = [(i,i) for n,i in enumerate(sorted(characters))])
	city = SelectField("Where are you from?", coerce=str,
		choices=[(i,i) for i in city_dict.keys()],
		validators=[Required()], 
		) #Requiring a region.
	submit = SubmitField("Submit")


class user(db.Model):
	'''Hello world'''
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(64), unique=False, nullable=True)
	lastName = db.Column(db.String(64), unique=False, nullable=True)
	userName = db.Column(db.String(64), unique=True, index=True, nullable=False)
	password_hash = db.Column(db.String(128), unique=False, index=False, nullable=False)
	birthdate = db.Column(db.DATE(), unique=False, nullable=True)
	email = db.Column(db.String(64), unique=True, nullable=True)
	vgCharacter = db.Column(db.String(64), unique=False, nullable=True)
	city = db.Column(db.String(64), unique=False, nullable=True)
	region = db.Column(db.String(64), unique=False, nullable=False)

	@property
	def password(self):
		raise AttributeError("Password is not a readable attribute")

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

class BlogForm(Form):
	"""docstring for BlogForm"""
	title = StringField("Title", validators=[Required()])
	body = StringField("Submit a blog post", validators=[Required()], widget=TextArea())
	submit = SubmitField("Submit")

		

class blogPosts(db.Model):
	"""docstring for blogPosts(db.model"""
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True, nullable=False)
	postText = db.Column(db.Text(), unique=True, nullable=False)
	region = db.Column(db.String(64), unique=False, nullable=False)
	date = db.Column(db.DATE(), unique=False, nullable=False, index=True)