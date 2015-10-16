import requests
import urllib
import re

urls = ["http://cnn.com", "http://networkworld.com", "http://cloudnewsdaily.com","https://www.alertlogic.com/"]
i=0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)
while i < len(urls):
    htmfile = urllib.urlopen(urls[i])
    htmtext = htmfile.read()
    titles=re.findall(pattern,htmtext)
    print titles
    i+=1

