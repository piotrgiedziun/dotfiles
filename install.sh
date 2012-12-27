#!/bin/bash
function pause() {
	python -c "raw_input('Press enter to continue...')"
}

echo "!! Next action will replace following files !!"
for file in {extra,bash_prompt,exports,aliases,functions}; do
	echo "> ~/.$file"
done

pause

for file in {extra,bash_prompt,exports,aliases,functions}; do
	echo "copy .$file to ~/.$file"
	cp ."$file" ~/."$file"
done

echo "downloading iterm2 style"
wget "https://raw.github.com/altercation/solarized/master/iterm2-colors-solarized/Solarized%20Dark.itermcolors"
open "Solarized Dark.itermcolors"
echo "set importet color sheme"

pause

echo "done!"