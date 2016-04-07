'''
Created on Apr 5, 2016

@author: Philip
'''
import urllib, urllib2
import json
from pprint import pprint
from datetime import datetime
'''
make a file 'myAPIKey.py' in the same directory as this library and in the file write:
API_KEY = '{your Guidebox API key}'
for example:
API_KEY = '123abc456def'
'''
from myAPIKey import API_KEY

BASE_API_URL = 'https://api-public.guidebox.com/v1.43'
REGION = 'US'
BASE_URL = BASE_API_URL + '/' + REGION + '/' + API_KEY

def tripleUrlEncode(s):
	for i in xrange(0,3):
		urllib.quote(s)
	return s

class artwork:
	def __init__(self, resolution, url):
		self.resolution = resolution
		self.url = url
	def __str__(self, *args, **kwargs):
		return \
			'URL: ' + str(self.url) + \
			'\nResolution: ' + str(self.resolution) + '\n'

class show():
	def __init__(self, gId, title, alternateTitles, containerShow, firstAired, imdbId, tvDb, theMovieDb, freebase, wikipediaId, tvRageId, tvRageLink, artwork):
		self.id = gId
		self.title = title
		self.alternateTitles = alternateTitles
		self.containerShow = containerShow
		self.firstAired = firstAired
		self.imdbId = imdbId
		self.tvDb = tvDb
		self.theMovieDb = theMovieDb
		self.freebase = freebase
		self.wikipediaId = wikipediaId
		self.tvRageId = tvRageId
		self.tvRageLink = tvRageLink
		self.artwork = artwork	
	
	def __str__(self, *args, **kwargs):
		text = \
			'Title: ' + str(self.title) + \
			'\nGuidebox ID:' + str(self.id) + \
			'\nAlternate Titles: ' + str(self.alternateTitles) + \
			'\nContainer Show: ' + str(self.containerShow) + \
			'\nFirst Aired: ' + str(self.firstAired.strftime('%Y-%m-%d')) + \
			'\nIMDb ID: ' + str(self.imdbId) + \
			'\nTVDB ID: ' + str(self.tvDb) + \
			'\nTheMovieDb ID: ' + str(self.theMovieDb) + \
			'\nFreebase ID: ' + str(self.freebase) + \
			'\nWikipedia ID:' + str(self.wikipediaId) + \
			'\nTVRage ID: ' + str(self.tvRageId) + \
			'\nTVRage Link: ' + str(self.tvRageLink) + \
			'\nArtwork: '
		for a in self.artwork:
			text += str(a)
		return text

class lookupShows():
	def __init__(self, channel = 'all', start = 0, numResults = 50, sources = 'all', platform = 'all', tags = [], 
				title = None, matchType = 'fuzzy', showId = None, site = 'imdb'):
		self.channel = channel
		self.start = start
		self.numResults = numResults
		self.sources = sources
		self.platform = platform
		self.tags = tags
		self.title = title
		self.matchType = matchType
		self.showId = showId
		self.site = site
		
		self.results = []
	
	def lookup(self):
		url = BASE_URL + '/'
		
		if (self.showId != None):
			url += 'search/id/' + \
					self.site + '/' + \
					self.showId			
		elif (self.title != None):
			url += 'search/title/' + \
					tripleUrlEncode(self.title) + '/' + \
					self.matchType
		else:
			url += 'shows/' + \
				self.channel + '/' + \
				str(self.start) + '/' + \
				str(self.numResults) + '/' + \
				self.sources + '/' + \
				self.platform + '/'
		
			tagStr = ''
			if len(self.tags) > 0:
				tagStr += '?'
				for tag in self.tags:
					tagStr += tag
				url += urllib.quote(tagStr)
			
		try:
			results = urllib2.urlopen(url).read()
		except urllib2.HTTPError as e:
			print('Error opening URL "' + url + ': ' + str(e))
			return False
		
		resultsDict = json.loads(results)
		
		self.totalResults = resultsDict['total_results'] if 'totalResults' in resultsDict else None
		self.totalReturned = resultsDict['total_returned'] if 'totalReturned' in resultsDict else None
		
		resultsListDict = dict() 
		if 'results' in resultsDict:
			resultsListDict = resultsDict['results']
		else:
			resultsListDict = [resultsDict]
		
		for s in resultsListDict:
			
			artworks = []
			artworkKeys = []
			for key in s.keys():
				if str(key).split('_')[0] == 'artwork':
					artworkKeys.append(key)
			for key in artworkKeys:
				artworks.append(artwork(key.split('_')[1], s[key]))
			
			self.results.append(show(
									s['id'],
									s['title'],
									s['alternate_titles'],
									s['container_show'],
									datetime.strptime(s['first_aired'], '%Y-%m-%d'),
									s['imdb_id'],
									s['tvdb'],
									s['themoviedb'],
									s['freebase'],
									s['wikipedia_id'],
									s['tvrage']['tvrage_id'],
									s['tvrage']['link'],
									artworks
									)
							)

		return True
	
	def __str__(self, *args, **kwargs):
		text = \
			'Total Results: ' + (str(self.totalResults) if hasattr(self.totalResults, 'totalResults') else 'not given') + \
			'\nResults Returned: ' + (str(self.totalReturned) if hasattr(self.totalResults, 'totalReturned') else 'not given') + '\n\n'
		
		for sh in self.results:
			text += str(sh) + '\n\n'
			
		return text

r = lookupShows(showId= 'tt0149460')
r.lookup()

print(r)