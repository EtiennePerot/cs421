import urllib2, json
from actors import *
from publishers import *
from authors import *
from genres import *
from languages import *
from video import *
import re

def splitStrings(myString):
	mySplit = myString.split(',')
	return mySplit

def createVideo(numVideos):
	successful = 0
	counter = 1
	while successful < numVideos:
		request = urllib2.Request(url='http://www.imdbapi.com/?i=' + str(counter))
		result = urllib2.urlopen(request)
		parsed = json.loads(result.read())
		if(parsed.has_key('Title')):
			print 'title: ' + parsed['Title']
			if(parsed.has_key('Year')):
				theDate =  parsed['Year'] + '-01' + '-01'
				print 'date: ' + theDate
			theFormat = 'DVD'
			print 'format: ' + theFormat
			if(parsed.has_key('Runtime')):
				print 'duration: ' + parsed['Runtime']
			print 'original language: English'
			if(parsed.has_key('Genre')):
				print 'genres: ' + parsed['Genre']
			if(parsed.has_key('Writer')):
				print 'author: ' + parsed['Writer']
			if(parsed.has_key('Director')):
				print 'director (publisher): ' + parsed['Director']
			if(parsed.has_key('Actors')):
				print 'actors: ' + parsed['Actors']
			print ''
			authors = splitStrings(parsed['Writer'])
			authorList = []
			for a in authors:
				lookup = authorByName(a.strip())
				if lookup is None:
					lookup = Author.create(name = a.strip())
				authorList.append(lookup)
			publishers = splitStrings(parsed['Director'])
			publisherList = []
			for a in publishers:
				lookup = publisherByName(a.strip())
				if lookup is None:
					lookup = Publisher.create(name = a.strip())
				publisherList.append(lookup)
			actors = splitStrings(parsed['Actors'])
			actorList = []
			for a in actors:
				lookup = actorByName(a.strip())
				if lookup is None:
					lookup = Actor.create(name = a.strip())
				actorList.append(lookup)
			genres = splitStrings(parsed['Genre'])
			genreList = genres
			try:
				Video.create(
					title = parsed['Title'],
					date = theDate,
					format = theFormat,
					duration = parsed['Runtime'],
					genres = genreList,
					authors = authorList,
					publishers = publisherList,
					actors = actorList,
					languages = ['en', 'fr']
				)
				successful += 1
			except:
				pass
