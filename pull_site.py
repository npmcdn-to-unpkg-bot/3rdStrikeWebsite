from subprocess import call
def Call(command):
	return call("{}".format(command), shell=True)
	
Call("git pull ThirdStrike master")
Call("git reset --hard ThirdStrike/master")
