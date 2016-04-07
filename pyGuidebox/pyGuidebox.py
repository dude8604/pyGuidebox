'''
Created on Apr 5, 2016

@author: Philip
'''
import urllib
import urllib2
import json
from pprint import pprint
from datetime import datetime
from ctypes import cast
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
	for i in xrange(0, 3):
		s = urllib.quote(s)
	return s


class artwork:

	def __init__(self, resolution, url):
		self.resolution = resolution
		self.url = url

	def __str__(self, *args, **kwargs):
		return \
			'URL: ' + str(self.url) + \
			'\nResolution: ' + str(self.resolution) + '\n'

def parseArtworks(result):
	artworks = []
	artworkKeys = []
	for key in result.keys():
		if str(key).split('_')[0] == 'artwork':
			artworkKeys.append(key)
	for key in artworkKeys:
		artworks.append(artwork(key.split('_')[1], result[key]))
	return artworks


class social:

	def __init__(self, facebookId, facebookLink, twitterId, twitterLink):
		self.facebookId = facebookId
		self.facebookLink = facebookLink
		self.twitterId = twitterId
		self.twitterLink = twitterLink

	def __str__(self, *args, **kwargs):
		return \
			'Facebook ID: ' + str(self.facebookId) + \
			'\nFacebook Link: ' + str(self.facebookLink) + \
			'\nTwitter ID: ' + str(self.twitterId) + \
			'\nTwitter Link: ' + str(self.twitterLink) + '\n'


class character:

	def __init__(self, actorName, actorId, characterName, ):
		self.actorName = actorName
		self.actorId = actorId
		self.characterName = characterName

	def __str__(self, *args, **kwargs):
		return \
			'Actor Name: ' + str(self.actorName) + \
			'\nActor ID: ' + str(self.actorId) + \
			'\nCharacter Name: ' + str(self.characterName) + '\n'


class idTitle:

	def __init__(self, tId, name):
		self.id = tId
		self.name = name

	def __str__(self, *args, **kwargs):
		return \
			'Name: ' + str(self.name) + \
			'\nID: ' + str(self.id) + '\n'


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
			'\nArtwork: \n'
		for a in self.artwork:
			text += str(a)+'\n'
		return text


class showDetailed(show):

	def __init__(self, gId, title, alternateTitles, containerShow, firstAired, imdbId, tvDb, theMovieDb, freebase,
				 wikipediaId, tvRageId, tvRageLink, artwork, status, network, channels, runtime, characters,
				 genres, tags, overview, airDay, airTime, rating, tvComId, metacritic, commonSenseMedia, socialNetworks, 
				 fanArt, poster, banner, url):
		show.__init__(self,
					  gId, title, alternateTitles, containerShow, firstAired, imdbId, tvDb, theMovieDb, freebase, wikipediaId, tvRageId, tvRageLink, artwork)
		self.status = status
		self.type = type
		self.network = network
		self.channels = channels  # a list of channel objects
		self.runtime = runtime
		self.cast = characters  # a list of character objects
		self.genres = genres  # a list of idTag objects
		self.tags = tags  # a list of idTag objects
		self.overview = overview
		self.airDay = airDay
		self.airTime = airTime
		self.rating = rating
		self.tvComId = tvComId
		self.metacritic = metacritic
		self.commonSenseMedia = commonSenseMedia
		self.social = socialNetworks  # a social object
		self.fanArt = fanArt
		self.poster = poster
		self.banner = banner
		self.url = url

	def __str__(self, *args, **kwargs):
		text = show.__str__(self, *args, **kwargs) + \
			'\nStatus: ' + str(self.status) + \
			'\nType: ' + str(self.type) + \
			'\nNetwork: ' + str(self.network) + \
			'\nChannels: \n'
		for ch in self.channels:
			text += str(ch)+'\n'
		text += '\nRuntime: ' + str(self.runtime) + \
				'Cast/Characters: \n'
		for c in self.cast:
			text += str(c)+'\n'
		text += '\nGenres: \n'
		for g in self.genres:
			text += str(g)+'\n'
		text += '\nTags: \n'
		for tag in self.tags:
			text += str(tag)+'\n'
		text += '\nOverview: ' + str(self.overview) + \
				'\nAir Day: ' + str(self.airDay) + \
				'\nAir Time: ' + str(self.airTime) + \
				'\nRating: ' + str(self.rating) + \
				'\nTV.com ID: ' + str(self.tvComId) + \
				'\nMetacritic ID: ' + str(self.metacritic) + \
				'\nCommon Sense Media ID: ' + str(self.commonSenseMedia) + \
				'\nSocial Media Info: ' + str(self.social) + \
				'\nFan Art URL: ' + str(self.fanArt) + \
				'\nPoster URL: ' + str(self.poster) + \
				'\nBanner URL: ' + str(self.banner) + \
				'\nGuidebox URL:' + str(self.url) + '\n\n'
				
		return text

class channel:
	def __init__(self, cId, name, shortName, channelType, artworks, imdbId, wikipediaId, socialNetworks, liveStreams, 
				primary):
		self.id = cId
		self.name=name
		self.shortName=shortName
		self.channelType=channelType
		self.artworks=artworks #list of artwork objects
		self.imdbId=imdbId
		self.wikipediaId=wikipediaId
		self.socialNetworks=socialNetworks #a social object
		self.liveStreams=liveStreams #streams object
		self.primary = primary
		
	def __str__(self, *args, **kwargs):
		text = \
			'Channel Name: '+str(self.name)+\
			'ID: '+str(self.id)+\
			'Short Name: '+str(self.shortName)+\
			'Channel Type: '+str(self.channelType)+\
			'Artworks: \n'
		for a in self.artworks:
			text += str(a)+'\n'
		text += '\nIMDb ID: '+str(self.imdbId)+\
				'\nWikipedia ID: '+str(self.wikipediaId)+\
				'\nSocial: '+str(self.socialNetworks)+\
				'\nLive Streaming Links: '+str(self.liveStreams)+\
				'\nIs Primary: '+str(self.primary)+'\n\n'
		return text


class streamingSource:
	
	def __init__(self, streamDict):
		self.source=streamDict['source']
		self.name=streamDict['display_name']
		self.channel=streamDict['tv_channel']
		self.type=streamDict['type']
		self.link=streamDict['link']
		self.isApp = 'app_name' in streamDict
		
		if self.isApp:
			self.appName = streamDict['app_name']
			self.appLink = streamDict['app_link']
			self.appRequired = True if streamDict['app_required'] == 1 else False
			self.appDownloadLink = streamDict['app_download_link']
	def __str__(self, *args, **kwargs):
		text = 'Source Name: '+str(self.source)+\
			'\nDisplay Name: '+str(self.name)+\
			'\nChannel: '+str(self.channel)+\
			'\nType: '+str(self.type)+\
			'\nLink: '+str(self.link)
		if self.isApp:
			text+= '\nApp Name: '+str(self.appName)+\
				'\nApp Link: '+str(self.appLink)+\
				'\nIs App Required for this Device? '+str(self.appRequired)+\
				'\nApp Download Link: '+str(self.appDownloadLink)
		return text + '\n\n'


class streams:
	
	def __init__(self, streamsDict):
		self.web = []#
		self.ios = []#streamsDict['ios']
		self.android = []#streamsDict['android']
		for s in streamsDict['web']:
			self.web.append(streamingSource(s))
		for s in streamsDict['ios']:
			self.ios.append(streamingSource(s))
		for s in streamsDict['android']:
			self.android.append(streamingSource(s))
	def __str__(self, *args, **kwargs):
		text = 'Web: \n'
		for s in self.web:
			text+=str(s)+'\n'
		text += 'iOS: \n'
		for s in self.ios:
			text+=str(s)+'\n'
		text = 'Android: \n'
		for s in self.android:
			text+=str(s)+'\n'
		return text

class lookupShows():

	def __init__(self, channel='all', start=0, numResults=50, sources='all', platform='all', tags=[],
				 title=None, matchType='fuzzy', showId=None, site='imdb'):
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
		self.firstLookup = True

	def lookup(self):
		'''
		Searches Guidebox for the criteria entered in the constructor
		'''
		if self.firstLookup:

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

			self.totalResults = resultsDict[
				'total_results'] if 'totalResults' in resultsDict else None
			self.totalReturned = resultsDict[
				'total_returned'] if 'totalReturned' in resultsDict else None

			resultsListDict = dict()
			if 'results' in resultsDict:
				resultsListDict = resultsDict['results']
			else:
				resultsListDict = [resultsDict]

			for s in resultsListDict:

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
					parseArtworks(s)
				)
				)

			self.firstLookup = False
			return True
		else:
			raise UserWarning('You already did up this search.')
			return False

	def lookupDetailed(self, index=None, gId=None):
		'''
		Look up more details about a show
		pass the Guidebox ID as gId, or the index in self.results after doing a lookup()
		'''
		gIdNum = None
		if gId == None and index != None:
			if self.firstLookup:
				raise Exception('You have to do a lookup() first.')
				return False
			if index > len(self.results):
				raise IndexError('Result index out of range')
				return False
			gIdNum = self.results[index].id
		elif gId != None:
			gIdNum = gId

		url = BASE_URL + '/show/' + str(gIdNum)

		try:
			results = urllib2.urlopen(url).read()
		except urllib2.HTTPError as e:
			print('Error opening URL "' + url + ': ' + str(e))
			return False

		resultDict = json.loads(results)

		channels = resultDict['channels']
		channelsList = []
		characters = resultDict['cast']
		charactersList=[]
		genres = resultDict['genres']
		genresList=[]
		tags = resultDict['tags']
		tagsList=[]
		
		#channels
		for ch in channels:
			channelsList.append(
							channel(
								ch['id'],
								ch['name'],
								ch['short_name'],
								ch['channel_type'],
								parseArtworks(ch),
								ch['external_ids']['imdb'],
								ch['external_ids']['wikipedia_id'],
								social(
									ch['social']['facebook']['facebook_id'],
									ch['social']['facebook']['link'],
									ch['social']['twitter']['twitter_id'],
									ch['social']['twitter']['link'],
									),
								streams(ch['live_stream']),
								ch['is_primary']
								)
							)
		for ch in characters:
			charactersList.append(
								character(
										ch['name'],
										ch['id'],
										ch['character_name']
										)
								)
			
		for g in genres:
			genresList.append(
								idTitle(
										g['id'],
										g['title']
										)
								)
			
		for t in tags:
			tagsList.append(
								idTitle(
										t['id'],
										t['tag']
										)
								)

		return showDetailed(
			resultDict['id'],
			resultDict['title'],
			resultDict['alternate_titles'],
			resultDict['container_show'],
			datetime.strptime(resultDict['first_aired'], '%Y-%m-%d'),
			resultDict['imdb_id'],
			resultDict['tvdb'],
			resultDict['themoviedb'],
			resultDict['freebase'],
			resultDict['wikipedia_id'],
			resultDict['tvrage']['tvrage_id'],
			resultDict['tvrage']['link'],
			parseArtworks(resultDict),
			resultDict['status'],
			resultDict['network'],
			channelsList,
			resultDict['runtime'],
			charactersList,
			genresList,
			tagsList,
			resultDict['overview'],
			resultDict['air_day_of_week'],
			resultDict['air_time'],
			resultDict['rating'],
			resultDict['tv_com'],
			resultDict['metacritic'],
			resultDict['common_sense_media'],
			social(
					resultDict['social']['facebook']['facebook_id'],
					resultDict['social']['facebook']['link'],
					resultDict['social']['twitter']['twitter_id'],
					resultDict['social']['twitter']['link']
				),
			resultDict['fanart'],
			resultDict['poster'],
			resultDict['banner'],
			resultDict['url']
		)

	def __str__(self, *args, **kwargs):
		text = ''
		try:
			text = 'Total Results: ' + (str(self.totalResults))
		except AttributeError, e:
			pass
		try:
			text += '\nResults Returned: ' + (str(self.totalReturned)) + '\n\n'
		except AttributeError, e:
			pass

		for sh in self.results:
			text += str(sh) + '\n\n'

		return text

r = lookupShows(title='the office')
r.lookup()
print(r.lookupDetailed(index=0))

print(r)
