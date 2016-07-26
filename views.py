from flask import Flask, request, render_template, session, redirect, url_for, flash
from run import app
from app import config, models
from app.models import *
from datetime import timedelta
import os

regions = []

@app.route("/", methods=["GET", "POST"])
def index():
	form = NameForm()
	if session.get('character') in ["Yun","Chun Li", "Ken"]:
			flash("Tier Whore")
	if session.get('character') =="Makoto":
		flash("You're a f****** Psycho")
	if form.validate_on_submit():

		old_name = session.get('username')
		if old_name != None and old_name != form.name.data:
			flash("Name updated")		
		name, age, character = form.name.data, form.age.data, form.character.data
		session['username'] = name
		session['character'] = character
		session['region'] = form.region.data
		regions.append(form.region.data)
		print(regions)
		return render_template("home.html", username=name, character=character)

	return render_template("home.html", form=form)

@app.route("/agent")
def browser_check():
	user_agent = request.headers.get('User-Agent')
	return "<p>Your browser is {}</p>".format(user_agent)

@app.route('/<username>')
def user_home(username=None, char=None):
	return render_template("home.html", username=username, char=char)

@app.route('/rankings/<region>')
def user_rankings(region):
	return render_template("rankings.html", region=session.get(region, None))

@app.route('/rankings')
def rankings():
	if session.get('username', None):
		if session.get('region', None):
			return render_template("rankings.html", username=session['username'], region=session['region'])	
		return render_template("rankings.html", username=session['username'])
	return render_template("rankings.html")

@app.route('/blog')
def blog():
	if session.get('region', None):
		return render_template("blog.html", data="Here's a customized blog for {}".format(session['region']))
	return render_template("blog.html", data="Non-region blog")
@app.route('/submit-your-story')
def blog_entry():
	if session.get('username', None):
		return "Okay"
	return "Jacked up"
@app.route('/logout', methods=["GET", "POST"])
def logout():
	session.clear()
	return redirect(url_for("index"))


