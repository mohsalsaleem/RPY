import sys
import unirest
import requests
import bs4
import feedzilla
import urllib2
import json
def createFile(n):
	print("Creating a new File")
	name = n
	try:	
		file = open(name,'w')
		file.close()
	except:
		print("Something Went Wrong")
		sys.exit(0)

def write(thelist):
	try:

		thefile = open("cleanFeed.txt",'w')
		for item in thelist:
			if "facebook" not in item:
				thefile.write("%s\n" % item)
		thefile.close()
	except:
		print("Soemthing went wrong")
		sys.exit(0)

def createSoup(url):
	website = url
	if "http://" not in url:
		website = "http://"+url
	response = requests.get(website)
	soup = bs4.BeautifulSoup(response.text)
	return soup

def crawl():
	with open("cleanFeed.txt") as thefile:
		cleanLinks = thefile.read().splitlines()
	count = 0
	for link in cleanLinks:
		try:"""
			soup = createSoup(link)
			print soup
			r = requests.get("http://api.feedzilla.com/v1/articles/search.json?q=Michael&count=1")
        		print r.content
        		"""
		except:
			continue
	# These code snippets use an open-source library.
		
	#response = unirest.get("https://devru-times-of-india.p.mashape.com/feeds/breakingnewsfeed.cms?feedtype=sjson",headers="X-Mashape-Key": "Bqzhz1udZPmshHmQ0P5dbnlxJuCgp1iozYsjsnhJemQBcFF8xO","Accept": "application/json"})
	# These code snippets use an open-source library. http://unirest.io/python
	"""
	response = unirest.get("https://devru-times-of-india.p.mashape.com/feeds/breakingnewsfeed.cms?feedtype=sjson",
  		headers={
    		"X-Mashape-Key": "Bqzhz1udZPmshHmQ0P5dbnlxJuCgp1iozYsjsnhJemQBcFF8xO",
    		"Accept": "application/json"
  				}
	)
	jsonResponse = response.body
	print json.dumps(jsonResponse,sort_keys = True, indent = 4)
	"""
	response1 = unirest.get("https://devru-times-of-india.p.mashape.com/feeds/feedurllist.cms?catagory=tech",
  		headers={
    		"X-Mashape-Key": "Bqzhz1udZPmshHmQ0P5dbnlxJuCgp1iozYsjsnhJemQBcFF8xO",
    		"Accept": "application/json"
  				}
	)
	
	#print json.dumps(response1.body,sort_keys = True, indent = 4)
	
	#if response1.body["Item"][0][""] :
	#json_object = json.load(response1.body)
	for i in response1.body["Item"]:
		if i["ID"] == "Tech-01":
			url =  i["defaulturl"]
			print url
			response2 = unirest.get(url)
			#print response2.body
			print json.dumps(response2.body,sort_keys = True, indent = 4)
			#soup = createSoup(url)
			#print soup.prettify()
			try:
				newsFile = open("newsFile.json","w")
				newsFile.write(json.dumps(response2.body,sort_keys = True, indent = 4))
				newsFile.close()
			except:
				print "MayDay MayDay"
				sys.exit(0)
			
	print response1.body["Item"][0]["ID"]
#	r = requests.get("http://api.feedzilla.com/v1/articles/search.json?q=Michael&count=1")
#	print r.content
	#print r.status_code

	print count
	
with open("postLink.txt") as f:
	postLink = f.read().splitlines()
#print postLink
createFile("cleanFeed.txt")
write(postLink)
crawl()
#print createSoup("http://www.google.com")

