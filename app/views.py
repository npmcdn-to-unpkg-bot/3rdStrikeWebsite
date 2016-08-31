from flask import Flask, session, request, render_template, redirect, url_for, flash
from flask.ext.sqlalchemy import Pagination
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from run import application, db
from app import config, models
from app.models import *
import os
from app.homepage_options import gen_results


# Home page parameters
start_date = "1-1-2016"
end_date = "2-1-2016"
start_date, end_date = None, None
leagues = sorted(["ChiStrike", "PSN"]) # Ensure these match with League Ids
LIVE = False #Don't forget to turn me on when you're ready to launch
# 

geographies = ["Overall"]
geographies += sorted(
	list(
		set(
			[i.city for i in user.query.all()])
		)
	)

@application.context_processor
def inject_locations():
	locData = Locations.query.all()
	return dict(locations=locData,
		geos=geographies,
		streams=Streams.query.all(),
		jinjaLocData=locData,
		live=LIVE,
		)

@application.route('/StreamPage')
def home():
	'''main page'''
	session.clear()
	return render_template("StreamPage.html")

@application.route("/")
@application.route("/index", methods=["GET"])
def index():
	eventQuery = Events.query.all()[::-1]
	blogs = blogPosts.query.filter_by(news="False")[::-1][:10] # Get 10 most recent blog posts
	news = blogPosts.query.filter_by(news="True")[::-1][:10]
	results_data = gen_results(start_date, end_date, leagues)
	vids = CoolVids.query.all()[::-1]
	session.clear()
	return render_template("index.html", news_articles=news, 
		blog_posts=blogs, events=eventQuery, league_data=results_data, start=start_date, end=end_date, vids=vids)

@application.route("/rankings")
def rankings_search():
	return '''Searchable rankings go here'''

@application.route("/news/<article>")
def news(article):
	postQuery = blogPosts.query.filter_by(title=article)[0]
	session.clear()
	return render_template('news.html', postData=postQuery)

@application.route("/under_construction")
def under_construction():
	return '''Under Construction'''

@application.route('/allBlogs')
def blog():
	blogs = blogPosts.query.all()[::-1]
	return render_template("blog.html", blogs=blogs)

# @application.route("/challenge")
# def challengePage():
# 	return render_template("challengePage.html")

# @application.route("/login", methods=["GET", "POST"])
# def login():
# 	form = LoginForm()
# 		# try:
# 		# 	if session['userName']:
# 		# 		otherPlayers = user.query.filter_by(region=session['location']).paginate()
# 		# 		return render_template('home.html', form=None, username=session['userName'],
# 		# 			results=otherPlayers, locations=gaming_places, geos=geographies)
# 		# except KeyError: pass #It's okay. Working on it now

# 		# if form.validate_on_submit():		
# 		# 	user_name = user.query.filter_by(userName=form.userName.data).first()
# 		# 	if user_name is None:
# 		# 		newUser = user()

# 		# 		newUser.userName = form.userName.data
# 		# 		newUser.password = form.password.data
# 		# 		newUser.firstName = form.firstName.data
# 		# 		newUser.lastName = form.lastName.data
# 		# 		newUser.email = form.email.data
# 		# 		newUser.vgCharacter = form.character.data
# 		# 		newUser.city = form.city.data
# 		# 		newUser.region = city_dict[form.city.data]
# 		# 		userNameCheck = user.query.filter_by(userName=newUser.userName)
# 		# 		passCheck = user.query.filter_by(password=newUser.password.data)
# 		# 		if userNameCheck & passCheck:
# 		# 			pass
# 		# 		else:
# 		# 			db.session.add(newUser)
# 		# 		try:
# 		# 			db.session.commit()
# 		# 		except (InvalidRequestError, IntegrityError):
# 		# 			flash("Welcome back {}".format(user_name))
# 		# 			db.session.delete(newUser)
# 		# 			return render_template("home.html", form=form, locations=gaming_places, geos=geographies)
# 		# 		db.session.delete(newUser)
# 		# 		flash("Registered!")
# 		# 		session['known'] = True
# 		# 	else:
# 		# 		flash("Welcome back {}".format(form.userName.data))
# 		# 		session['known'] = False
# 		# 	session['userName'] = form.userName.data
# 		# 	session['city'] = form.city.data
# 		# 	session['location'] = city_dict[form.city.data]
# 		# 	session['region'] = city_dict[form.city.data]
# 		# 	otherPlayers = user.query.filter_by(region=session['location']).paginate()
# 		# 	return render_template('home.html', form=None, username=session['userName'], 
# 		# 		results=otherPlayers, locations=gaming_places, geos=geographies)
# 	return render_template("login.html", form=form)

@application.route('/logout', methods=["GET", "POST"])
def logout():
	session.clear()
	return redirect(url_for("index"))