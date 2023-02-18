import os
import re
import sys, getopt


ispath = 1

opts, args = getopt.getopt(sys.argv[1:],"hp:")
for opt, arg in opts:
	if opt == '-h':
		print ('find.py -p[0..2]')
		sys.exit()
	elif opt in ("-p"):
		ispath = arg


for root, dirs, files in os.walk("."):
	for file in files:
		actual = root + '/' + file
		if(actual[-9:]=='kicad_sch'):
			with open(actual,"r") as file_one:
				if(int(ispath)==2):
					print(actual+" ==>")
				patrn = "text \"([^\"]*)"
				for line in file_one:
					group = re.search(patrn, line)
					if(group):
						if(int(ispath)==0):
							print(group[1])
						if(int(ispath)==1):
							print(actual+" - " + group[1])
						if(int(ispath)==2):
							print("\t"+group[1])

