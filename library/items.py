from base import *
from authors import *
from genres import *
from publishers import *
from languages import *

itemsTable = dbTable("""CREATE TABLE `items` (
  `iid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`iid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
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

booksTable = dbTable("""CREATE TABLE `books` (
  `iid` int(10) unsigned NOT NULL COMMENT 'Item ID',
  `isbn` bigint(20) unsigned NOT NULL,
  `pages` int(10) unsigned NOT NULL,
  PRIMARY KEY (`iid`),
  KEY `isbn` (`isbn`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
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
