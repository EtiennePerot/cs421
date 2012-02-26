import urllib2, json
import library
from library.dateutil.dateutil.parser import parse
import re
for i in range(10):
    request = urllib2.Request(url='https://www.googleapis.com/books/v1/volumes?q=intitle:' + str(i) + '&maxResults=40')
    result = urllib2.urlopen(request)
    parsed_result = json.loads(result.read())
    book_list = parsed_result['items']
    for item in book_list:
        if item['volumeInfo'].has_key('title') and item['volumeInfo'].has_key('industryIdentifiers') and item['volumeInfo'].has_key('pageCount'):
            try:
                date_value = item['volumeInfo']['publishedDate']
                year = re.search('\d+', date_value)
                if year.group(0)<1900:
                    date_value = str(year)
                else:
                    date_value = parse(date_value).strftime('%y-%m-%d')
                library.items.Book.create(
                    title=item['volumeInfo']['title'],
                    date=date_value,
                    isbn=item['volumeInfo']['industryIdentifiers'][0]['identifier'],
                    pages=item['volumeInfo']['pageCount']
                )
            except:
                pass
            