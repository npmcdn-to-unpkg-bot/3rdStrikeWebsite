from subprocess import call
def Call(command):
	return call("{}".format(command), shell=True)
	
Call("git pull origin master")
Call("git reset --hard origin/master")
