installPackages.py

from subprocess import call

packages = "flask", "wtforms", "wtforms_html5", "sqlalchemy","flask-admin ", "flask-wtf"
for i in packages:
	try : call("pip install {}".format(i), shell=True)
	except:
	print("Failed to install {}".format(i))