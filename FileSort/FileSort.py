import os
import shutil
import sys

# path for inclusion-file
includePath = os.path.dirname(os.path.realpath(__file__)) + "/include.txt"

# create inclusion-file in script directory if not exists
try:
	include = open(includePath, "r").read().split("\n")
except IOError:
	print("No include.txt found")
	print("creating " + includePath)
	fInc =  open(includePath, "w")
	fInc.write("included extensions - one per line")
	fInc.close()
	sys.exit()

# read all files with extensions in inclusion-file
files = [f for f in os.listdir('.') if os.path.isfile(f) and f[f.rfind(".") + 1 :len(f) : 1].lower() in include]

# get all existing directories
directories = [d for d in os.listdir('.') if os.path.isdir(d)]

# add extensions to dirToCreate if not exist
dirToCreate =  set([f[f.rfind(".") + 1 :len(f) : 1].lower() for f in files if f[f.rfind(".") + 1 :len(f) : 1].lower() not in directories])

# creates missing directories
print(str(len(dirToCreate)) + " Directories created")
for d in dirToCreate:
	os.mkdir("./" + d)
	print ("- " + d)

# moves loose files
print(str(len(files)) + " Files moved")
for f in files:
	extension = f[f.rfind(".") + 1 :len(f) : 1].lower()
	shutil.move(f, ("./" + extension + "/" + f))
	print ("- " + f)
 
