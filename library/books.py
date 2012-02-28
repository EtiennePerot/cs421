from base import *
from items import *

# Books
booksTable = dbTable("""CREATE TABLE `books` (
  `iid` int(10) unsigned NOT NULL COMMENT 'Item ID',
  `isbn` bigint(10) unsigned zerofill NOT NULL,
  `pages` int(10) unsigned NOT NULL,
  PRIMARY KEY (`iid`),
  UNIQUE KEY `isbn` (`isbn`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
_rawBookClass = booksTable.genClass()
class Book(_rawBookClass):
	@staticmethod
	def create(title, date, isbn, pages, genres=[], authors=[], publishers=[], languages=[]):
		# Languages are all "subtitled" in books
		i = Item.create(title, date, genres, authors, publishers, languageForceType(languages, HasLanguage.type_subtitled))
		return _rawBookClass.create(iid=i['iid'], isbn=isbn, pages=pages)
booksTable.bindClass(Book)
