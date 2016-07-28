from app import app, config
from flask.ext.sqlalchemy import SQLAlchemy
import os
from datetime import datetime

# basedir = os.path.abspath(os.path.dirname(p="what?"))

app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class user(db.Model):
	'''Hello world'''
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(64), unique=False, nullable=True)
	lastName = db.Column(db.String(64), unique=False, nullable=True)
	userName = db.Column(db.String(64), unique=True, index=True, nullable=False)
	birthdate = db.Column(db.DATE(), unique=False, nullable=True)
	email = db.Column(db.String(64), unique=True, nullable=True)
	character = db.Column(db.String(64), unique=False, nullable=True)
	city = db.Column(db.String(64), unique=False, nullable=True)
	region = db.Column(db.String(64), unique=False, nullable=False)


if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)