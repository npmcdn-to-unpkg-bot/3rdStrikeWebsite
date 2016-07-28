# installPackages.py

from subprocess import call

packages = "flask", "flask-bootstrap", "wtforms", "wtforms_html5",\
"sqlalchemy","flask-admin ", "flask-wtf", "flask-alchemy", "flask-admin"
for i in packages:
	try : call("pip install {}".format(i), shell=True)
	except:	print("Failed to install {}".format(i))