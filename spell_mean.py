import urllib2,html5lib

def word_meaning(word):
	s = "http://wordnetweb.princeton.edu/perl/webwn?s="
	s += word
	f = urllib2.urlopen(s)
	#print f.read()

inp = raw_input()
fetched_page = word_meaning(str(inp))
document = html5lib.parse(fetched_page)
print document