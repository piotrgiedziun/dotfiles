#!/usr/bin/python
import os

print "!! Next action will replace following files !!"
for file in ["extra","bash_prompt","exports","aliases","functions"]:
	print "> ~/%s" % (file, )

a = raw_input('\nDo you want to replace dotfiles? (y/n)\n')

if a.lower() == "y":
	for file in ["extra","bash_prompt","exports","aliases","functions"]:
		os.system("cp .%s ~/.%s" % (file, file))

a = raw_input('\nDo you want to install project list file? (y/n)\n')

if a.lower() == "y":
	os.system("cp list.py ~/Projects/list.py")
	os.system("chmod +x ~/Projects/list.py")

a = raw_input("\nDo you want to download iterm2 style? (y/n)\n")

if a.lower() == "y":
	os.system("wget 'https://raw.github.com/altercation/solarized/master/iterm2-colors-solarized/Solarized%20Dark.itermcolors'")
	os.system("open 'Solarized Dark.itermcolors'")
	print "set importet color sheme"