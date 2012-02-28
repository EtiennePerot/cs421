from base import *
from items import *

# Magazines
magazinesTable = dbTable("""CREATE TABLE `magazines` (
  `iid` int(10) unsigned NOT NULL,
  `issn` bigint(8) unsigned zerofill NOT NULL,
  `issue` int(10) unsigned NOT NULL,
  `pages` int(10) unsigned NOT NULL,
  PRIMARY KEY (`iid`),
  KEY `issn` (`issn`),
  CONSTRAINT `magazines_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
_rawMagazineClass = magazinesTable.genClass()
class Magazine(_rawMagazineClass):
	@staticmethod
	def create(title, date, issn, issue, pages, genres=[], authors=[], publishers=[], languages=[]):
		# Languages are all "subtitled" in magazines
		i = Item.create(title, date, genres, authors, publishers, languageForceType(languages, HasLanguage.type_subtitled))
		return _rawMagazineClass.create(iid=i['iid'], issn=issn, issue=issue, pages=pages)
magazinesTable.bindClass(Magazine)

def populateSampleMagazines():
	import magazines_sample
	magazines_sample.run()
