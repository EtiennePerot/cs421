import urllib2, json
import library
#from library.dateutil.dateutil.parser import parse
import re
#import  imdb

for i in range(50):
    request = urllib2.Request(url='http://www.imdbapi.com/?i=' + str(i)) 

#'https://www.googleapis.com/books/v1/volumes?q=intitle:'+str(i) +'&maxResults=40')

    result = urllib2.urlopen(request)
    parsed = json.loads(result.read())
#    video_list = parsed_result['items']
#    for item in video_list:
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
        
        library.items.Video.create(
            title = parsed['Title'],
            date = theDate,
            format = theFormat,
            duration = parsed['Runtime']
        )
            
        

#for i in range(5):
#note iid generated automatically
       # print 'title'
       # print 'date'
    #note choose this randomly
       # print 'format'
       # print 'duration' 
       # print 'original language'
    #note choose English French automatically, and Spanish occasionally
       # print 'genres'
       # print 'author'
       # print 'publisher/studio'
       # print 'actors' 
