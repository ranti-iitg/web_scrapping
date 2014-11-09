from collections import defaultdict

import pandas as pd
import matplotlib.pyplot as plt
import requests
from pattern import web

url = 'http://en.wikipedia.org/wiki/List_of_countries_by_past_and_future_population'
website_html = requests.get(url).text.encode("utf-8")
#print website_html

def get_population_html_table(html):
	dom = web.Element(html)
	tbls=dom.by_class('sortable wikitable')
	return tbls

	
tables= get_population_html_table(website_html)
for t in tables:
	print t.attributes
