from flask import Flask
from app import config
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy


application = Flask(__name__)

bootstrap = Bootstrap(application)

application.config.from_object(config)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
application.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(application)
db.create_all()

from app import views