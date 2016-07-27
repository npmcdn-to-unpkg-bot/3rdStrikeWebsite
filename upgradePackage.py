from subprocess import call

call("pip freeze >> packages.txt")

with open("packages.txt", "r+") as packs:
	packages = packs.readlines()

	for pack in packages:
		print(pack)
		pass
	# try : call("pip install {} -U".format(pack), shell=True)
	# except:	print("Failed to install {}".format(pack))