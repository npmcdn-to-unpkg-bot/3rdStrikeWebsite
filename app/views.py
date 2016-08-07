from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask.ext.sqlalchemy import Pagination
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from run import application, db
from app import config, models
from app.models import *
from datetime import timedelta, datetime
import os


allRegions = user.query.all()
geographies = ["Overall"]+sorted(list(set([i.city for i in allRegions])))

locData = Locations.query.all()
gaming_places = {k.Name: k.url for k in locData}
nameAddress_dict = {k.Name : [k.Lat, k.Lon] for k in locData}

@application.route("/")
def index():
	return render_template("home.html", 
		locations=gaming_places, geos=geographies)

@application.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
		# try:
		# 	if session['userName']:
		# 		otherPlayers = user.query.filter_by(region=session['location']).paginate()
		# 		return render_template('home.html', form=None, username=session['userName'],
		# 			results=otherPlayers, locations=gaming_places, geos=geographies)
		# except KeyError: pass #It's okay. Working on it now

		# if form.validate_on_submit():		
		# 	user_name = user.query.filter_by(userName=form.userName.data).first()
		# 	if user_name is None:
		# 		newUser = user()

		# 		newUser.userName = form.userName.data
		# 		newUser.password = form.password.data
		# 		newUser.firstName = form.firstName.data
		# 		newUser.lastName = form.lastName.data
		# 		newUser.email = form.email.data
		# 		newUser.vgCharacter = form.character.data
		# 		newUser.city = form.city.data
		# 		newUser.region = city_dict[form.city.data]
		# 		userNameCheck = user.query.filter_by(userName=newUser.userName)
		# 		passCheck = user.query.filter_by(password=newUser.password.data)
		# 		if userNameCheck & passCheck:
		# 			pass
		# 		else:
		# 			db.session.add(newUser)
		# 		try:
		# 			db.session.commit()
		# 		except (InvalidRequestError, IntegrityError):
		# 			flash("Welcome back {}".format(user_name))
		# 			db.session.delete(newUser)
		# 			return render_template("home.html", form=form, locations=gaming_places, geos=geographies)
		# 		db.session.delete(newUser)
		# 		flash("Registered!")
		# 		session['known'] = True
		# 	else:
		# 		flash("Welcome back {}".format(form.userName.data))
		# 		session['known'] = False
		# 	session['userName'] = form.userName.data
		# 	session['city'] = form.city.data
		# 	session['location'] = city_dict[form.city.data]
		# 	session['region'] = city_dict[form.city.data]
		# 	otherPlayers = user.query.filter_by(region=session['location']).paginate()
		# 	return render_template('home.html', form=None, username=session['userName'], 
		# 		results=otherPlayers, locations=gaming_places, geos=geographies)
	return render_template("login.html", form=form)


@application.route("/register", methods=["GET", "POST"])
def register():
	form = NameForm()
	if form.validate_on_submit():
		# Check if username or email in database
		checkName = form.userName
		# if 
			# Alert if username or email taken
		# if not, add to db session and push to db
		# then push to main page w/ session
	return render_template("register.html", form=form, 
		locations=nameAddress_dict,
		keyItems = tuple(i for i in nameAddress_dict.keys())
		)



@application.route("/agent")
def browser_check():
	user_agent = request.headers.get('User-Agent')
	return "<p>Your browser is {}</p>".format(user_agent)

@application.route('/rankings')
def rankings():
	if session.get('username', None):
		blogQuery = blogPosts.query.filter_by(region=session['location']).paginate()
		return render_template("rankings.html", username=session['username'], locations=gaming_places, geos=geographies)
	blogQuery = blogPosts.query.all()
	return render_template("rankings.html", locations=gaming_places, geos=geographies)

@application.route('/rankings/<region>')
def region_rankings(region):
	return render_template("rankings.html",region=region, locations=gaming_places, geos=geographies)

@application.route('/blog', methods=["GET","POST"])
def blog():
	mostRecentBlog = blogPosts.query.all()[-1]
	if session.get('region'):
		blogForm = BlogForm()
		if blogForm.validate_on_submit():
			newBlogPost = blogPosts()
			newBlogPost.title = blogForm.title.data
			newBlogPost.postText = blogForm.body.data
			newBlogPost.region = session.get('region')
			newBlogPost.date = datetime.now()

			db.session.add(newBlogPost)
			try:
				db.session.commit()
				flash("Blog posted!")
				return render_template("blog.html", form=blogForm, recent=mostRecentBlog, blogData=posts,
					locations=gaming_places, geos=geographies)				
			except:
				flash("Failed to post plog... Sry, my bad.")

		posts = blogPosts.query.filter_by(region=session.get('region')).paginate().items[:-1]

		return render_template("blog.html", form=blogForm, recent=mostRecentBlog, blogData=posts,
			locations=gaming_places, geos=geographies)
	posts = blogPosts.query.paginate().items[:-1]
	return render_template("blog.html", recent=mostRecentBlog, blogData=posts, 
		locations=gaming_places, geos=geographies)

@application.route('/blog/<article>')
def blogReader(article):
	post = blogPosts.query.filter_by(title=article)[0]
	return render_template("blogPage.html", articleName=article, postText=post.postText)


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


