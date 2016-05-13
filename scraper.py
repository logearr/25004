import urllib2
import os.path
from bs4 import BeautifulSoup

URL = "http://www.imdb.com/list/ls058374907/?start=1&view=compact&sort=listorian:asc&defaults=1&scb=0.3063102242919442"

def get_html():
	if os.path.isfile("cache.html"):
		f = open("cache.html")
		data = f.read()
		f.close()
		return data
	else:
		data = urllib2.urlopen(URL).read()
		f = open("cache.html", "w")
		f.write(data)
		f.close()
		return data

html = get_html()

soup = BeautifulSoup(html, "html.parser");

#items = [item for item in soup.select(".list_item") if "data-item-id" in item.attrs ]
items = soup.find_all("td", class_="title")

for item in items:
	print "<li>%s</li>" % item.contents[0].string


