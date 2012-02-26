import urllib2, json
import library
from library.authors import *
from library.publishers import *
from library.actors import *
from library.genres import *
import re

def splitStrings(myString):
    mySplit = myString.split(',')
    return mySplit

n = 50

#updating i here gets n film id's: note that not all will be valid!
for i in range(n):
    request = urllib2.Request(url='http://www.imdbapi.com/?i=' + str(i)) 
    result = urllib2.urlopen(request)
    parsed = json.loads(result.read())

    #print parsed attributes
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

#here
        authors = splitStrings(parsed['Writer'])#authorByName(parsed['Writer'])
        #if author is None:
        #    author = Author.create(parsed['Writer'])
        authorList = []
        for a in authors:
            lookup = authorByName(a.strip())
            if lookup is None:
                lookup = Author.create(name = a.strip())
            authorList.append(lookup)

#here
        publishers = splitStrings(parsed['Director'])#publisherByName(parsed['Director'])  
        #if publisher is None:
        #    publisher = Publisher.create(parsed['Director'])
        publisherList = []
        for a in publishers:
            lookup = publisherByName(a.strip())
            if lookup is None:
                lookup = Publisher.create(name = a.strip())
            publisherList.append(lookup)

#here            
        actors = splitStrings(parsed['Actors'])#actorByName(parsed['Actors'])
        #if actor is None:
        #    actor = Actor.create(parsed['Actors'])
        actorList = []
        for a in actors:
            lookup = actorByName(a.strip())
            if lookup is None:
                lookup = Actor.create(name = a.strip())
            actorList.append(lookup)
        
        genres = splitStrings(parsed['Genre'])
        genreList = genres
#        for a in genres:
#            lookup = genreByName(a.strip())
#            if lookup is None:
#                lookup = Genre.create(name = a.strip())
#            genreList.append(a)

        library.items.Video.create(
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
        
