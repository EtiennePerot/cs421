from base import *
from items import *

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

def generateRandomVideo(numVideos):
	import video_generator
	video_generator.createVideo(numVideos)
