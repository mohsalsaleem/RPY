import json
import urllib2
import requests
from pprint import pprint


with open("newsFile.json") as jsonFile:
	data = json.load(jsonFile)
pprint(data)
responses = []
for item in data["NewsItem"]:
	title = item["HeadLine"]
	content = item["Caption"]
	r = requests.post("https://kceg.herokuapp.com/messages.json?message[name]="+title+"&message[message]="+content)
	responses.append(r.status_code)
print responses

#r = requests.post("https://kceg.herokuapp.com/messages.json?message[name]=saleem&message[phone]=123456789")

#print r.status_code

