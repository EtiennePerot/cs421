import urllib2, json
for i in range(10):
    request = urllib2.Request(url='https://www.googleapis.com/books/v1/volumes?q=intitle:' + str(i) + '&maxResults=40')
    result = urllib2.urlopen(request)
    parsed_result = json.loads(result.read())
    book_list = parsed_result['items']
    for item in book_list:
        if item['volumeInfo'].has_key('title') and item['volumeInfo'].has_key('industryIdentifiers') and item['volumeInfo'].has_key('pageCount'):
            print 'isbn:' + item['volumeInfo']['industryIdentifiers'][0]['identifier']
            print 'title:' + item['volumeInfo']['title']
            print 'pages:' + str(item['volumeInfo']['pageCount'])
            print 'release date:' + item['volumeInfo']['publishedDate'] + '\n'
