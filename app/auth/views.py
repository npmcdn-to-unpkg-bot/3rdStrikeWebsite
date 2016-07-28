from flask import render_template
from . import auth


@app.route("/login")
def login():
	return render_template('auth/login.html')