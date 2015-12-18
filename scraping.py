from bs4 import BeautifulSoup
import requests
from urllib2 import HTTPError
import urllib as UR

try:
	page = UR.urlopen("http://www.computerworld.com")
except IOError:
	print("URL Not Found")
		#continue
else:

	soup = BeautifulSoup(page.read(), "html.parser")
	htag = soup.findAll({"h4"}) 
	for n in htag:
		print n

# print (type(htag))
# print("-----------------------")

# paragraphs = []
# for x in htag:
#     paragraphs = paragraphs.append(str(x))
#     print paragraphs
# #print htag


