from flask import Flask, request, render_template, session, redirect, url_for, flash
from models import NameForm
from run import app
from app import config
from datetime import timedelta
import os


@app.route("/", methods=["GET", "POST"])
def index():
	form = NameForm()
	if form.validate_on_submit():

		old_name = session.get('username')
		if old_name != None and old_name != form.name.data:
			flash("Name updated")
		name, age, character = form.name.data, form.age.data, form.character.data
		session['username'] = name
		session['character'] = character
		session.permanent = True
		try: session['counter'] += 1
		except KeyError: session['counter'] = 0

		return render_template("home.html", username=name, character=character)

	return render_template("home.html", form=form)

@app.route("/agent")
def browser_check():
	user_agent = request.headers.get('User-Agent')
	return "<p>Your browser is {}</p>".format(user_agent)

@app.route('/<username>')
def user_home(username=None, char=None):
	return render_template("home.html", username=username, char=char)

# @app.route('/rankings/<username>')
# def user_rankings(username):
# 	return render_template("rankings.html", username=session.get(username))

@app.route('/rankings')
def rankings():
	if session.get('username', None):
		return render_template("rankings.html", username=session['username'])
	return render_template("rankings.html")

@app.route('/blog')
def blog():
	if session.get('username', None):
		return render_template("blog.html", data="Okay")
	return render_template("blog.html", data="Nothing here")
@app.route('/submit-your-story')
def blog_entry():
	if session.get('username', None):
		return "Okay"
	return "Jacked up"
@app.route('/logout')
def logout():
	session.clear()
	return index()


