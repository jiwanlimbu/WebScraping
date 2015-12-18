import requests
import urllib #access internet and network request
import re
from bs4 import BeautifulSoup

url = "http://www.networkworld.com"

head = [url]

while len(head) > 0 :
	try:	
		htmltext = urllib.urlopen(head[0]).read()
	except:
		
		print head[0]
	soup = BeautifulSoup(htmltext, "html.parser")	
	
	head.pop(0)

	for tag in soup.findAll('<h4>','</h4>'):
		print tag[0]
#print htmltext
#code = '<h4>(.+?)</h4>'
#---------------------------------- file open -------------------
# f = open('code.txt', 'w')
# f.writelines(htmltext)
# f.close()
# f = open('code.txt')
# line = f.readlines()
# print line[0:20]
# 	for i in line:
# 		x = ....(i)
# 	#print code
# #else:
# print ('it doesnt match or somthing')

# pattern = re.compile(reg)
# head = re.findall(pattern,htmltext)
# print head
#------------------------------------------------------------------
# http = httplib2.Http()
# status, response = http.request('http://www.nytimes.com')

# for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print link['href']
