from base import *

authorsTable = dbTable("""CREATE TABLE `authors` (
  `auid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`auid`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
Author = authorsTable.genClass()

def authorByName(name):
	return authorsTable.findSingle(name=name)

authoredByTable = dbTable("""CREATE TABLE `authored_by` (
  `iid` int(10) unsigned NOT NULL COMMENT 'Item ID',
  `auid` int(10) unsigned NOT NULL COMMENT 'Author ID',
  PRIMARY KEY (`iid`,`auid`),
  KEY `auid` (`auid`),
  CONSTRAINT `authored_by_ibfk_2` FOREIGN KEY (`auid`) REFERENCES `authors` (`auid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `authored_by_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
AuthoredBy = authoredByTable.genClass()

if __name__ == '__main__':
	authoredByTable.drop()
	authorsTable.drop()
	authorsTable.create()
	authoredByTable.create()
	Author.create(name='Cory Doctorow')
	Author.create(name='Albert Camus')
	Author.create(name='Victor Hugo')
	Author.create(name='Samuel Beckett')
	Author.create(name='Balzac')
	print authorByName('Albert Camus')
