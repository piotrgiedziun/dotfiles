#!/usr/bin/python
import os, sys

dirs = []
filter = None

if len(sys.argv) > 1:
	filter = sys.argv[1]

i = 1
for dir in [o for o in os.listdir('.') if os.path.isdir(o)]:
	if filter == None or filter in dir:
		dirs.append(dir)
		print "[%d] %s" % (i, dir)
		i+=1

print "cd to: "