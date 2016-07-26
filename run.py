from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap
from app import app, config
import os


app.config.from_object(config)

if __name__ == '__main__':
	app.run(debug=True)