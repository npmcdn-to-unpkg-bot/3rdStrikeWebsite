from app import application, db
from flask import Flask
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.migrate import Migrate, MigrateCommand

import os
from datetime import datetime

if __name__ == '__main__':
	# migrate = Migrate(application, db)

	application.run(debug=True)