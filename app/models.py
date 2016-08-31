from flask_wtf import Form
from numpy import nan
from run import db
from datetime import date
from wtforms import StringField, SelectField, SubmitField, TextField, validators
from wtforms.widgets import TextArea
from wtforms.fields.html5 import DateField, EmailField
from wtforms.validators import Required
from werkzeug.security import generate_password_hash, check_password_hash
from app.lookUp import characters, city_dict


cities = sorted([i for i in city_dict.keys()])


class NameForm(Form):
	firstName = StringField("First name", validators=[Required()])
	lastName = StringField("Last name", validators=[Required()])
	userName = StringField("Enter a Username", validators=[Required()])
	password = StringField("Enter a password", validators=[Required()])
	email = EmailField("Email")
	character = SelectField("Who's your favorite character?", coerce=str, 
		choices = [(i,i) for n,i in enumerate(sorted(characters))])
	city = SelectField("Where are you from?", coerce=str,
		choices=[(i,i) for i in cities],
		validators=[Required()], 
		) #Requiring a region.
	submit = SubmitField("Submit")


class LoginForm(Form):
	userName = StringField("Username", validators=[Required()])
	password = StringField("Password", validators=[Required()])
	submit = SubmitField("Submit")

class BlogForm(Form):
	"""docstring for BlogForm"""
	title = StringField("Title", validators=[Required()])
	body = StringField("Submit a blog post", validators=[Required()], widget=TextArea())
	submit = SubmitField("Submit")


class Locations(db.Model):
	'''Hello world'''
	__tablename__ = 'Locations'
	id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(64))
	Address = db.Column(db.String(64))
	City = db.Column(db.String(64))
	State = db.Column(db.String(64))
	Country = db.Column(db.String(64))
	Lat = db.Column(db.Float())
	Lon = db.Column(db.Float())
	url = db.Column(db.String(64))


class Streams(db.Model):
	__tablename__ = 'streams'
	id = db.Column(db.Integer, primary_key=True)
	cleanName = db.Column(db.String(64))
	link = db.Column(db.String(64))
	chats = db.Column(db.String(64))
	channelName = db.Column(db.String(64))
	priority = db.Column(db.Integer)


class CoolVids(db.Model):
	__tablename__ = 'coolVids'
	id = db.Column(db.Integer, primary_key=True)
	iframe = db.Column(db.String(64))

class Events(db.Model):
	'''Hello world'''
	__tablename__ = 'events'
	id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(64))
	Price = db.Column(db.Float())
	City = db.Column(db.String(64))
	State = db.Column(db.String(64))
	Country = db.Column(db.String(64))
	Lat = db.Column(db.Float())
	Lon = db.Column(db.Float())
	url = db.Column(db.String(64))
	image_url = db.Column(db.String(64))


class user(db.Model):
	'''Hello world'''
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(64), unique=False, nullable=True)
	lastName = db.Column(db.String(64), unique=False, nullable=True)
	userName = db.Column(db.String(64), unique=True, index=True, nullable=False)
	password_hash = db.Column(db.String(128), unique=False, index=False, nullable=False)
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


class matchLog(db.Model):
	'''Hello world'''
	__tablename__ = 'matchLog'
	id = db.Column(db.Integer, primary_key=True)
	p1 = db.Column(db.String(64))
	p2 = db.Column(db.String(64))
	char1 = db.Column(db.String(64))
	char2 = db.Column(db.String(64))
	eventID = db.Column(db.Integer)
	winnerID = db.Column(db.Integer)
	date = db.Column(db.String(64))
	league = db.Column(db.String(64))


class playerDB(db.Model):
	'''Hello world'''
	__tablename__ = 'playerDB'
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(64), unique=False, nullable=True)
	lastName = db.Column(db.String(64), unique=False, nullable=True)
	alias = db.Column(db.String(64), unique=True, index=True, nullable=False)
	# password_hash = db.Column(db.String(128), unique=False, index=False, nullable=False)
	# email = db.Column(db.String(64), unique=True, nullable=True)
	# vgCharacter = db.Column(db.String(64), unique=False, nullable=True)
	city = db.Column(db.String(64), unique=False, nullable=True)
	state = db.Column(db.String(64), unique=False, nullable=False)


class blogPosts(db.Model):
	"""docstring for blogPosts(db.model"""
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True, nullable=False)
	postText = db.Column(db.Text(), unique=True, nullable=False)
	region = db.Column(db.String(64), unique=False, nullable=False)
	date = db.Column(db.DATE(), unique=False, nullable=False, index=True)
	image_link = db.Column(db.String(64), unique=False, nullable=False)
	author = db.Column(db.String(64), unique=False, nullable=False)
	author_image = db.Column(db.String(64), unique=False, nullable=True)
	news = db.Column(db.String(64), unique=False, nullable=False)
