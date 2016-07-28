from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask.ext.sqlalchemy import Pagination
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from run import application, db
from app import config, models
from app.models import *
from datetime import timedelta, datetime
import os


gaming_places = {"Logan Arcade": "http://loganarcade.com", 
"Next Level Battle Lounge" : "http://nycnextlevel.com",
"Astro City Arcade" : "http://arcadeufo.com"}

geographies = ["Overall"]+sorted(["Chicago","Atlanta", "New York City"])


@application.route("/", methods=["GET", "POST"])
def index():
	form = NameForm()
	try: print(session['userName'])
	except: print("No session")
	try:
		if session['userName']:
			otherPlayers = user.query.filter_by(region=session['location']).paginate()
			return render_template('home.html', form=None, username=session['userName'],
				results=otherPlayers, locations=gaming_places, geos=geographies)
	except KeyError: pass #It's okay. Working on it now
	if form.validate_on_submit():		
		user_name = user.query.filter_by(userName=form.userName.data).first()
		if user_name is None:
			newUser = user()
			newUser.firstName, newUser.lastName, newUser.userName,\
			newUser.birthdate, newUser.email, newUser.vgCharacter,\
			newUser.city, newUser.region, newUser.password\
			=\
			form.firstName.data, form.lastName.data, form.userName.data,\
			form.birthdate.data, form.email.data, form.character.data,\
			form.city.data, city_dict[form.city.data], form.password.data
			db.session.add(newUser)
			try:
				db.session.commit()
			except:
				flash("Welcome back {}".format(user_name))
				return render_template("home.html", form=form, locations=gaming_places, geos=geographies)		
			flash("Registered!")
			session['known'] = True
		else:
			flash("Welcome back {}".format(form.userName.data))
			session['known'] = False
		session['userName'] = form.userName.data
		session['city'] = form.city.data
		session['location'] = city_dict[form.city.data]
		otherPlayers = user.query.filter_by(region=session['location']).paginate()
		return render_template('home.html', form=None, username=session['userName'], 
			results=otherPlayers, locations=gaming_places, geos=geographies)
	return render_template("home.html", form=form, locations=gaming_places, geos=geographies)
	return '''Not working'''
@application.route("/agent")
def browser_check():
	user_agent = request.headers.get('User-Agent')
	return "<p>Your browser is {}</p>".format(user_agent)

# @application.route('/<username>')
# def user_home(username=None, char=None):
# 	return render_template("home.html", username=username, char=char, locations=gaming_places, geos=geographies)

@application.route('/rankings')
def rankings():
	if session.get('username', None):
		return render_template("rankings.html", username=session['username'], locations=gaming_places, geos=geographies)
	return render_template("rankings.html", locations=gaming_places, geos=geographies)

@application.route('/rankings/<region>')
def region_rankings(region):
	return render_template("rankings.html",region=region, locations=gaming_places, geos=geographies)

@application.route('/blog')
def blog():
	if session.get('region', None):
		return render_template("blog.html", data="Here's a customized blog for {}".format(session['region']), locations=gaming_places, geos=geographies)
	return render_template("blog.html", data="Non-region blog", locations=gaming_places, geos=geographies)

@application.route('/submit-your-story')
def blog_entry():
	if session.get('username', None):
		return temp()
	return "Jacked up"

@application.route('/logout', methods=["GET", "POST"])
def logout():
	session.clear()
	return redirect(url_for("index"))

@application.route('/temp')
def temp():

	return "Go back, there's nothing here yet"


