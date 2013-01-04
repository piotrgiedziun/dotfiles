#!/usr/bin/python
import os

files = ["extra","bash_prompt","exports","aliases","functions","gitconfig"]

print "!! Next action will replace following files !!"
for file in files:
	print "> ~/%s" % (file, )

a = raw_input('\nDo you want to replace dotfiles? (y/n)\n')

if a.lower() == "y":
	for file in files:
		os.system("cp .%s ~/.%s" % (file, file))
	print "remember to edit ~/.gitconfig in ordet to enter your valid data"

a = raw_input('\nDo you want to install project list file? (y/n)\n')

if a.lower() == "y":
	os.system("cp list.py ~/Projects/list.py")
	os.system("chmod +x ~/Projects/list.py")

a = raw_input("\nDo you want to download iterm2 style? (y/n)\n")

if a.lower() == "y":
	os.system("wget 'https://raw.github.com/altercation/solarized/master/iterm2-colors-solarized/Solarized%20Dark.itermcolors'")
	os.system("open 'Solarized Dark.itermcolors'")
	print "open iterm and set downloaded color sheme"