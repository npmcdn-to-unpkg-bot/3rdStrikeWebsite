from flask import Flask, request, render_template, session, redirect, url_for, flash
from run import app
from app import config, models
from app.models import *
from datetime import timedelta
import os
gaming_places = {"Logan Arcade": "http://loganarcade.com", 
"Next Level Battle Lounge" : "http://nycnextlevel.com",
"Astro City Arcade" : "http://arcadeufo.com"}

@app.route("/", methods=["GET", "POST"])
def index():
	form = NameForm()
	if session.get('character') in ["Yun","Chun Li", "Ken"]:
			flash("Tier Whore")
	if session.get('character') =="Makoto":
		flash("You're a f****** Psycho Makoto player")
	if form.validate_on_submit():

		old_name = session.get('username')
		if old_name != None and old_name != form.name.data:
			flash("Name updated")		
		name, age, character = form.name.data, form.age.data, form.character.data
		session['username'] = name
		session['character'] = character
		session['region'] = form.region.data
		
		return render_template("home.html", username=name, character=character, locations=gaming_places)

	return render_template("home.html", form=form, locations=gaming_places)

@app.route("/agent")
def browser_check():
	user_agent = request.headers.get('User-Agent')
	return "<p>Your browser is {}</p>".format(user_agent)

@app.route('/<username>')
def user_home(username=None, char=None):
	return render_template("home.html", username=username, char=char, locations=gaming_places)

@app.route('/rankings')
def rankings():
	if session.get('username', None):
		if session.get('region', None):
			return render_template("rankings.html", username=session['username'], region=session['region'], locations=gaming_places)
		return render_template("rankings.html", username=session['username'], locations=gaming_places)
	return render_template("rankings.html", locations=gaming_places)

@app.route('/blog')
def blog():
	if session.get('region', None):
		return render_template("blog.html", data="Here's a customized blog for {}".format(session['region']), locations=gaming_places)
	return render_template("blog.html", data="Non-region blog", locations=gaming_places)

@app.route('/submit-your-story')
def blog_entry():
	if session.get('username', None):
		return temp()
	return "Jacked up"

@app.route('/logout', methods=["GET", "POST"])
def logout():
	session.clear()
	return redirect(url_for("index"))

@app.route('/temp')
def temp():

	return "Go back, there's nothing here yet"


