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
itemsTable.bindClass(Item)

# Books
booksTable = dbTable("""CREATE TABLE `books` (
  `iid` int(10) unsigned NOT NULL COMMENT 'Item ID',
  `isbn` bigint(13) unsigned zerofill NOT NULL,
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

# Songs
songsTable = dbTable("""CREATE TABLE `songs` (
 `iid` int(10) unsigned NOT NULL,
 `track` int(10) unsigned NOT NULL,
 `title` varchar(255) DEFAULT NULL,
 `duration` int(10) unsigned DEFAULT NULL,
 PRIMARY KEY (`iid`,`track`),
 CONSTRAINT `songs_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
Song = songsTable.genClass()

# Audio
audioTable = dbTable("""CREATE TABLE `audio` (
 `iid` int(10) unsigned NOT NULL COMMENT 'Item ID',
 `format` enum('vinyl','cd','digital') NOT NULL,
 PRIMARY KEY (`iid`),
 CONSTRAINT `audio_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
_rawAudioClass = audioTable.genClass()
class Audio(_rawAudioClass):
	@staticmethod
	def create(title, date, format, songs=[], genres=[], authors=[], publishers=[], languages=[]):
		"""
		songs are dictionaries of the form {
			'track': trackNumber,
			'title': 'Song title',
			'duration': trackDuration
		}
		"""
		# Languages are all "spoken" in audio
		i = Item.create(title, date, genres, authors, publishers, languageForceType(languages, HasLanguage.type_spoken))
		a = _rawAudioClass.create(iid=i['iid'], format=format)
		for s in songs:
			Song.create(iid=i['iid'], **s)
		return a
Audio.format_vinyl = 'vinyl'
Audio.format_cd = 'cd'
Audio.format_digital = 'digital'
audioTable.bindClass(Audio)

# Video
videoTable = dbTable("""CREATE TABLE `video` (
 `iid` int(10) unsigned NOT NULL,
 `format` enum('vhs','dvd','bluray','digital') NOT NULL,
 `duration` int(10) unsigned NOT NULL,
 PRIMARY KEY (`iid`),
 CONSTRAINT `video_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
_rawVideoClass = videoTable.genClass()
class Video(_rawVideoClass):
	@staticmethod
	def create(title, date, format, duration, actors=[], genres=[], authors=[], publishers=[], languages=[]):
		"""
		actors is a list of Actor records or actor IDs.
		"""
		# If language type is not given, assume it is spoken
		i = Item.create(title, date, genres, authors, publishers, languageAssumeType(languages, HasLanguage.type_spoken))
		for a in actors:
			HasActor.create(iid=i['iid'], aid=a)
		return _rawVideoClass.create(iid=i['iid'], format=format, duration=duration)
Video.format_vhs = 'vhs'
Video.format_dvd = 'dvd'
Video.format_bluray = 'bluray'
Video.format_digital = 'digital'
videoTable.bindClass(Video)

# Instances
instancesTable = dbTable("""CREATE TABLE `instances` (
 `instid` int(10) unsigned NOT NULL COMMENT 'Instance ID',
 `iid` int(10) unsigned NOT NULL COMMENT 'Item ID',
 PRIMARY KEY (`instid`),
 KEY `iid` (`iid`),
 CONSTRAINT `instances_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
Instance = instancesTable.genClass()

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
