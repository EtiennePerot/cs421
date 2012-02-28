import urllib2, json
from books import *
import time
from dateutil.dateutil.parser import parse
import re
import sys

def createBooks(numBooks):
	books_generated = 0
	i = 0
	while books_generated < numBooks:
		request = urllib2.Request(url='https://www.googleapis.com/books/v1/volumes?q=isbn:' + str(i) + '&maxResults=40')
		i += 1
		time.sleep(5)
		try:
			result = urllib2.urlopen(request)
			book_list = json.loads(result.read())['items']
			for item in book_list:
				if item.has_key('volumeInfo') and item['volumeInfo'].has_key('publishedDate')  and item['volumeInfo'].has_key('title') and item['volumeInfo'].has_key('industryIdentifiers') and item['volumeInfo'].has_key('pageCount'):
					year = re.search('\d+', item['volumeInfo']['publishedDate'])
					if year.group(0) < 1900:
						published_date = year.group(0) + '-01-01'
					else:
						published_date = parse(item['volumeInfo']['publishedDate']).strftime('%y-%m-%d')
					Book.create(
						title=item['volumeInfo']['title'],
						date=published_date,
						isbn=re.search('\d+', item['volumeInfo']['industryIdentifiers'][0]['identifier']).group(0),
						pages=item['volumeInfo']['pageCount']
					)
					books_generated += 1
					print 'Number of books generated:', str(books_generated)
		except Exception as detail:
			print detail
			pass
