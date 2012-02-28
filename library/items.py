from base import *
from authors import *
from genres import *
from publishers import *
from languages import *
from actors import *

# Items
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
		"""
		languages are dictionaries of the form {
			'iso': 'isoCode',
			'type': HasLanguage.type_something
		}
		"""
		i = _rawItemClass.create(title=title, date=date)
		for g in genres:
			Genre.create(iid=i['iid'], name=g)
		for a in authors:
			AuthoredBy.create(iid=i['iid'], auid=a)
		for p in publishers:
			PublishedBy.create(iid=i['iid'], pid=p)
		for l in languages:
			HasLanguage.create(iid=i['iid'], **l)
		return i
	def makeInstance(self):
		return Instance.create(iid=self['iid'])
itemsTable.bindClass(Item)

# Instances
instancesTable = dbTable("""CREATE TABLE `instances` (
  `instid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Instance ID',
  `iid` int(10) unsigned NOT NULL COMMENT 'Item ID',
  PRIMARY KEY (`instid`),
  KEY `iid` (`iid`),
  CONSTRAINT `instances_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
_rawInstanceClass = instancesTable.genClass()
class Instance(_rawInstanceClass):
	def reserve(self, member, fromDate, toDate, type):
		"""
			Sadly, due to "from" being a keyword in Python, we cannot use it as argument names.
			So the "from" has been renamed to "fromDate" in this function, and "to" has been renamed to "toDate" for consistency.
		"""
		return ReservedBy.create(pnid=member, instid=self['instid'], to=toDate, type=type, **{'from': fromDate}) # Hax to make it have a keyword argument named "from"
instancesTable.bindClass(Instance)

# Reservations
reservedByTable = dbTable("""CREATE TABLE `reserved_by` (
 `pnid` int(10) unsigned NOT NULL,
 `instid` int(10) unsigned NOT NULL,
 `from` date NOT NULL,
 `to` date NOT NULL,
 `type` enum('borrowed','reserved') NOT NULL,
 PRIMARY KEY (`pnid`,`instid`),
 KEY `instid` (`instid`),
 KEY `type` (`type`),
 CONSTRAINT `reserved_by_ibfk_1` FOREIGN KEY (`pnid`) REFERENCES `people` (`pnid`) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT `reserved_by_ibfk_2` FOREIGN KEY (`instid`) REFERENCES `instances` (`instid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
ReservedBy = reservedByTable.genClass()
ReservedBy.type_borrowed = 'borrowed'
ReservedBy.type_reserved = 'reserved'

def generateRandomItemInstances():
	import random
	allItems = itemsTable.getAll()
	for item in allItems:
		numInstances = random.randint(0, 8)
		for i in xrange(numInstances):
			item.makeInstance()

def generateRandomReservations():
	import time, random, people
	allInstances = instancesTable.getAll()
	allMembers = people.membersTable.getAll()
	possibleReservationTypes = (ReservedBy.type_borrowed, ReservedBy.type_reserved)
	for instance in allInstances:
		if random.randint(0, 9) > 6: # Only reserved with a certain priority
			member = random.choice(allMembers)
			fromTime = time.time() - random.randint(1, 3 * 24 * 3600)
			fromDate = time.strftime('%Y-%m-%d', time.localtime(fromTime))
			toDate = time.strftime('%Y-%m-%d', time.localtime(fromTime + random.randint(3 * 24 * 3600, 15 * 24 * 3600)))
			reservationType = random.choice(possibleReservationTypes)
			instance.reserve(member, fromDate, toDate, reservationType)

if __name__ == '__main__':
	makeRandomItemInstances()
