from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask.ext.sqlalchemy import Pagination
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from run import app, db, user
from app import config, models
from app.models import *
from datetime import timedelta, datetime
import os

gaming_places = {"Logan Arcade": "http://loganarcade.com", 
"Next Level Battle Lounge" : "http://nycnextlevel.com",
"Astro City Arcade" : "http://arcadeufo.com"}

geographies = ["Overall"]+sorted(["Chicago","Atlanta", "New York City"])

@app.route("/", methods=["GET", "POST"])
def index():
	form = NameForm()
	if session.get('character') in ["Yun","Chun Li", "Ken"]:
			flash("Tier Whore")
	if session.get('character') =="Makoto":
		flash("You're a f****** Psycho Makoto player")
	if form.validate_on_submit():		
		newUser = user()
		newUser.firstName, newUser.lastName, newUser.userName,\
		newUser.birthdate, newUser.email, newUser.character, newUser.city, newUser.region\
		=\
		form.firstName.data, form.lastName.data, form.userName.data,\
		form.birthdate.data, form.email.data, form.character.data, form.city.data, city_dict[form.city.data]

		try:
			db.session.add(newUser)
			db.session.commit()
		except IntegrityError as dataTaken:
			db.session.delete(newUser)
			flash("Username or email already taken")
			return render_template("home.html", form=form, locations=gaming_places, geos=geographies)

		name, age, character = form.userName.data, form.birthdate.data, form.character.data

		
		session['username'] = name
		session['character'] = character
		# session['region'] = form.city.data
		try:

			query = user.query.filter_by(region=city_dict[form.city.data])
			return render_template("home.html", username=name, character=character, results=query, locations=gaming_places, geos=geographies)
		except InvalidRequestError:
			return render_template("home.html", form=form, locations=gaming_places, geos=geographies)
	
	return render_template("home.html", form=form, locations=gaming_places, geos=geographies)
	

@app.route("/agent")
def browser_check():
	user_agent = request.headers.get('User-Agent')
	return "<p>Your browser is {}</p>".format(user_agent)

@app.route('/<username>')
def user_home(username=None, char=None):
	return render_template("home.html", username=username, char=char, locations=gaming_places, geos=geographies)

@app.route('/rankings')
def rankings():
	if session.get('username', None):
		# if session.get('region', None):
		# 	return render_template("rankings.html", username=session['username'], region=session['region'], locations=gaming_places, geos=geographies)
		return render_template("rankings.html", username=session['username'], locations=gaming_places, geos=geographies)
	return render_template("rankings.html", locations=gaming_places, geos=geographies)

@app.route('/rankings/<region>')
def region_rankings(region):
	return render_template("rankings.html",region=region, locations=gaming_places, geos=geographies)

@app.route('/blog')
def blog():
	if session.get('region', None):
		return render_template("blog.html", data="Here's a customized blog for {}".format(session['region']), locations=gaming_places, geos=geographies)
	return render_template("blog.html", data="Non-region blog", locations=gaming_places, geos=geographies)

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


