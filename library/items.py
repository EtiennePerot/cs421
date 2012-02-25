from base import *
from authors import *
from genres import *
from publishers import *
from languages import *

itemsTable = dbTable('items', '*iid', 'title', 'date')
_rawItemClass = itemsTable.genClass()
class Item(_rawItemClass):
	@staticmethod
	def create(title, date, genres=[], authors=[], publishers=[], languages=[]):
		i = _rawItemClass.create(title=title, date=date)
		for g in genres:
			Genre.create(iid=i['iid'], name=g)
		for a in authors:
			AuthoredBy.create(iid=i['iid'], auid=a)
		for p in publishers:
			PublishedBy.create(iid=i['iid'], pid=p)
		for l in languages:
			HasLanguage.create(iid=i['iid'], type=HasLanguage.type_subtitled, iso=l)
		return i
itemsTable.bindClass(Item)

booksTable = dbTable('books', '*iid', 'isbn', 'pages')
_rawBookClass = booksTable.genClass()
class Book(_rawBookClass):
	@staticmethod
	def create(title, date, isbn, pages, genres=[], authors=[], publishers=[], languages=[]):
		i = Item.create(title, date, genres, authors, publishers, languages)
		return _rawBookClass.create(iid=i['iid'], isbn=isbn, pages=pages)
booksTable.bindClass(Book)

if __name__ == '__main__':
	Book.create(
		title      = 'The Stranger',
		date       = '1942-01-01',
		isbn       = 9780679720201,
		pages      = 124,
		genres     = ['Existentialism', 'Philosophy'],
		authors    = [authorByName('Albert Camus')],
		publishers = [publisherByName('Freshbooks')],
		languages  = ['en', 'fr']
	)
