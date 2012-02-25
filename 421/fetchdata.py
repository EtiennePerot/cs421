import  urllib2, json
for i in range(100):
    request = urllib2.Request(url='https://www.googleapis.com/books/v1/volumes?q=intitle:'+str(i))
    result = urllib2.urlopen(request)
    parsed_result = json.loads(result.read())
    book_list = parsed_result['items']
    for item in book_list:
        if(item['volumeInfo'].has_key('title')):
            print item['volumeInfo']['title']