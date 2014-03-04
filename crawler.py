import re
import urllib
from bs4 import BeautifulSoup

url="http://apple.com"
lvl=0
emailList = []

urlChecked = []

def crawling(link, level):
	print "LEVEL: ",level 
	html = urllib.urlopen(link)
	soup = BeautifulSoup(html)

	for email in soup.find_all('a'):
		email=email.get('href')
		if email is not None:
			check=email.encode('ascii', 'ignore')
			if ( (re.search( r'mailto:\w+',check) ) or (re.search( r'\w+@\w+\.\w{2,6}\.?\w*',check) ) ):
				emailList.append(check)

	for url in soup.find_all('a'):
		#print url.get('href')
		url = url.get('href')
		if url is not None:
			url=url.encode('ascii', 'ignore')
			if ( not(re.search( r'http[s]?:\/\/[w.-]*', url)) and (re.search( r'\/[w.-/]*', url)) ):
				if (link[-1:]== '/'):
					link = link[:1]
				url = link+url
			print url
			if ( (re.search( r'http:\/\/[\w.-]*', url ))):
				if (not(re.search(r'http:\/\/(google|\w+\.google|www\.youtube|goo\.gl|www\.facebook\.com|www\.twitter\.com|t\.co)[w.-]*', url))):
					if (level<1):
						if url not in urlChecked:
							urlChecked.append(url)
							crawling(url, level+1)


crawling(url,lvl)

semiFinalList=[]
#Remove Mail to from email ids
for mail in emailList:
	if ((re.search( r'mailto:\w+',mail)) ):
		mail = mail[7:]
		semiFinalList.append(mail);

#Remove Duplicates 
finalList = []
for mail in semiFinalList:
	if mail not in finalList:
		finalList.append(mail)

print "Email IDs Found: "
for mail in finalList:
	print mail