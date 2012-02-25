from base import *

publishersTable = dbTable("""CREATE TABLE `publishers` (
  `pid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Publisher ID',
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
Publisher = publishersTable.genClass()

def publisherByName(name):
	return publishersTable.findSingle(name=name)

publishedByTable = dbTable("""CREATE TABLE `published_by` (
  `iid` int(10) unsigned NOT NULL COMMENT 'Item ID',
  `pid` int(10) unsigned NOT NULL COMMENT 'Publisher ID',
  PRIMARY KEY (`iid`,`pid`),
  KEY `pid` (`pid`),
  CONSTRAINT `published_by_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `publishers` (`pid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `published_by_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
PublishedBy = publishedByTable.genClass()

if __name__ == '__main__':
	# Sample data
	Publisher.create(name='Hachette')
	Publisher.create(name='Freshbooks')
	Publisher.create(name='First Choice')
	Publisher.create(name='Room To Read')
	Publisher.create(name='Xlibris')
