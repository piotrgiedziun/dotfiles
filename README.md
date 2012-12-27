#Peter's dotfiles
This is a collection of dotfiles customised for my own usage.<br>
Based on [Roderik's dotfiles](https://github.com/roderik/dotfiles) and [Matt's dotfiles](https://github.com/mattbanks/dotfiles)

##Feature

###Navigation
<table width="100%">
  <tr>
    <th>Alias</th><th>Method</th><th>Description</th>
  </tr><tr>
  	<td> ..</td><td>```cd ..```</td><td> </td>
	 </tr><tr>
		<td> ...</td><td>```cd ../..```</td><td> </td>
	 </tr><tr>
		<td> ~</td><td>```cd ~```</td><td> </td>
	 </tr><tr>
		<td> home</td><td>```cd ~```</td><td> </td>
	 </tr><tr>
		<td> d</td><td>```cd ~/Dropbox```</td><td> </td>
	 </tr><tr>
		<td> p</td><td>```cd ~/Projects```</td><td> </td>
	 </tr>
</table>
###Opening files
<table width="100%">
  <tr>
   <th>Alias</th><th>Method</th><th>Description</th>
  </tr>
	 <tr>
		<td> o</td><td>```open```</td><td> </td>
	 </tr><tr>
		<td> o.</td><td>```open .```</td><td> </td>
	 </tr>
</table>
###Listing
<table width="100%">
  <tr>
    <th>Alias</th><th>Method</th><th>Description</th>
  </tr>
	 <tr>
		<td> lsl</td><td>```ls -l```</td><td> </td>
	 </tr><tr>
		<td> lsa</td><td>```ls -la```</td><td> </td>
	 </tr><tr>
		<td> lsd</td><td>'ls -l | grep "^d"'</td><td> </td>
	 </tr>
</table>
###Network
<table width="100%">
  <tr>
   <th>Alias</th><th>Method</th><th>Description</th>
  </tr>
	<tr>
		<td> server</td><td>function</td><td>host python SimpleHTTPServer in current directory. Port mifgh be given as parm (port)</td>
	 </tr><tr>
		<td> ip</td><td>```dig +short myip.opendns.com @resolver1.opendns.com```</td><td>return ip </td>
	 </tr><tr>
		<td> localip</td><td>```ipconfig getifaddr en1```</td><td> return local ip</td>
	 </tr><tr>
		<td> whois</td><td>```whois -h whois-servers.net```</td><td> </td>
	 </tr><tr>
		<td> flush</td><td>```dscacheutil -flushcache && killall -HUP mDNSResponder```</td><td>flush DNS </td>
	 </tr><tr>
		<td> sniff</td><td>```sudo ngrep -d 'en1' -t '^(GET|POST) ' 'tcp and port 80'```</td><td>sniff HTTP </td>
	 </tr><tr>
		<td> httpdump</td><td>```sudo tcpdump -i en1 -n -s 0 -w - | grep -a -o -E \"Host\: .*|GET \/.*\"```</td><td> </td>
	 </tr>
	 <tr>
		<td> json</td><td>function</td><td>Syntax-highlight JSON strings or files</td>
	 </tr><tr>
		<td> GET|POST |PUT|DELETE [url]</td><td>```lwp-request -m '[METHOD]'```</td><td> send GET/POST/PUT/DELETE request</td>
	 </tr>
</table>
###Others
<table width="100%">
  <tr>
    <th>Alias</th><th>Method</th><th>Description</th>
  </tr><tr>
		<td> mkd</td><td>function</td><td>make dir and cd to it</td>
	 </tr><tr>
<tr>
		<td> copy</td><td>function</td><td>copy content to clipboard (```copy cat file.txt```)</td>
	 </tr><tr>
		<td> dataurl</td><td>function</td><td>return base64 of given object</td>
	 </tr>
	  <tr>
		<td> update</td><td>```sudo softwareupdate -i -a; brew update; brew upgrade; npm update npm -g; npm update -g; sudo gem update```</td><td>global update </td>
	 </tr><tr>
		<td> lscleanup</td><td>```/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user && killall Finder```</td><td> </td>
	 </tr><tr>
		<td> cleanup</td><td>```find . -type f -name '*.DS_Store' -ls -delete```</td><td>clean up dir </td>
	 </tr><tr>
		<td> emptytrash</td><td>```sudo rm -rfv /Volumes/*/.Trashes; sudo rm -rfv ~/.Trash; sudo rm -rfv /private/var/log/asl/*.asl```</td><td> </td>
	 </tr><tr>
		<td> urlencode</td><td>```python -c "import sys, urllib as ul; print ul.quote_plus(sys.argv[1]);"```</td><td> </td>
	 </tr><tr>
		<td> mergepdf</td><td>```/System/Library/Automator/Combine\ PDF\ Pages.action/Contents/Resources/join.py```</td><td> merge PDF files</td>
	 </tr>
</table>

##Directory structure
* **~/Projects** - project main dir

##Prerequisites
* **brew** - The missing package manager for OS X [[download]](http://mxcl.github.com/homebrew/)<br>
```ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"```
* **wget** - The non−interactive network downloader<br>
```brew install wget```

##Installation
Open terminal and type
```bash
git clone https://github.com/piotrgiedziun/dotfiles.git && cd dotfiles && ./install.sh
```
