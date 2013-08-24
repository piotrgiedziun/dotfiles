#Peter's dotfiles
This is a collection of dotfiles customised for my own usage.<br>
Based on [Roderik's dotfiles](https://github.com/roderik/dotfiles) and [Matt's dotfiles](https://github.com/mattbanks/dotfiles)

##Feature

###Navigation
<table width="100%">
  <tr>
    <th>Alias</th><th>Method</th><th>Description</th>
  </tr>
  	<tr>
		<td> cdf</td><td>(fuction)</td><td> cd to path indicated by Finder.app instance</td>
	 </tr><tr>
		<td> ..</td><td>cd ..</td><td> cd up</td>
	 </tr><tr>
		<td> ...</td><td>cd ../..</td><td> cd 2 x up</td>
	 </tr><tr>
		<td> ~</td><td>cd ~</td><td> cd to home directory</td>
	 </tr><tr>
		<td> -</td><td>cd -</td><td> cd to previously visted folder</td>
	 </tr><tr>
		<td> cdd</td><td>cd ~/Downloads</td><td> </td>
	 </tr><tr>
		<td> cdp</td><td>cd ~/Projects</td><td> </td>
	 </tr><tr>
		<td> cdw</td><td>cd ~/Work</td><td> </td>
	 </tr>
</table>
###Opening files
<table width="100%">
  <tr>
   <th>Alias</th><th>Method</th><th>Description</th>
  </tr>
	 <tr>
		<td> o</td><td>open</td><td> </td>
	 </tr><tr>
		<td> o.</td><td>open .</td><td> </td>
	 </tr>
</table>
###Listing
<table width="100%">
  <tr>
    <th>Alias</th><th>Method</th><th>Description</th>
  </tr>
	 <tr>
		<td> ll</td><td>ls -l</td><td> </td>
	 </tr><tr>
		<td> la</td><td>ls -la</td><td> </td>
	 </tr><tr>
		<td> lsd</td><td>ls -l | grep "^d"</td><td> </td>
	 </tr>
</table>
###Network
<table width="100%">
  <tr>
   <th>Alias</th><th>Method</th><th>Description</th>
  </tr>
	<tr>
		<td> server</td><td>function</td><td>host python SimpleHTTPServer in current directory. Port might be given as parm (port)</td>
	 </tr><tr>
		<td> ip</td><td>dig +short myip.opendns.com @resolver1.opendns.com</td><td>return ip </td>
	 </tr><tr>
		<td> localip</td><td>ipconfig getifaddr en1</td><td> return local ip</td>
	 </tr><tr>
		<td> whois</td><td>whois -h whois-servers.net</td><td> </td>
	 </tr><tr>
		<td> flush</td><td>dscacheutil -flushcache && killall -HUP mDNSResponder</td><td>flush DNS </td>
	 </tr><tr>
		<td> sniff</td><td>sudo ngrep -d 'en1' -t '^(GET|POST) ' 'tcp and port 80'</td><td>sniff HTTP </td>
	 </tr><tr>
		<td> httpdump</td><td>sudo tcpdump -i en1 -n -s 0 -w - | grep -a -o -E \"Host\: .*|GET \/.*\"</td><td> </td>
	 </tr>
	 <tr>
		<td> json</td><td>function</td><td>Syntax-highlight JSON strings or files</td>
	 </tr><tr>
		<td> GET|POST|PUT|DELETE [url]</td><td>lwp-request -m '[METHOD]'</td><td> send GET/POST/PUT/DELETE request</td>
	 </tr>
</table>
###Others
<table width="100%">
  <tr>
    <th>Alias</th><th>Description</th><th>Usage</th>
  </tr><tr>
		<td> mkd</td><td>make dir and cd to it</td><td>mkd iLikePizza</td>
	 </tr><tr>
<tr>
		<td> copy</td><td>copy given content to clipboard </td><td>copy cat ~/.ssh/id_rsa.pub</td>
	 </tr><tr>
		<td> dataurl</td><td>dataurl image.png</td><td>return base64 of given object</td>
	 </tr>
	  <tr>
		<td> update</td><td>update</td><td>update gem, brew, system etc.</td>
	 </tr><tr>
		<td> lscleanup</td><td>lscleanup</td><td> clean up given dir</td>
	 </tr><tr>
		<td> cleanup</td><td>cleanup</td><td>clean up current dir</td>
	 </tr><tr>
		<td> emptytrash</td><td>emptytrash</td><td> clean trash</td>
	 </tr><tr>
		<td> urlencode</td><td>urlencode http://google.com</td><td> encode given url</td>
	 </tr><tr>
		<td> mergepdf</td><td>mergepdf --output out.pdf file1.pdf file2.pdf</td><td> merge PDF files</td>
	 </tr><tr>
		<td> bell</td><td>sleep 2 && bell</td><td> notify task is done</td>
	 </tr>
</table>

##Directory structure
* **~/Projects** - own projects main dir
* **~/Work** - work projects main dir

##Prerequisites
* **brew** - The missing package manager for OS X [[download]](http://mxcl.github.com/homebrew/)<br>
ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
* **wget** - The non−interactive network downloader<br>
brew install wget

##Installation
Open terminal and type
```bash
git clone https://github.com/piotrgiedziun/dotfiles.git && cd dotfiles && ./install
```
