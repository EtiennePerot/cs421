from base import *
from items import *

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

def populateSampleAudio():
	import audio_sample
	audio_sample.run()
