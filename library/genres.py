from base import *

genresTable = dbTable("""CREATE TABLE `genres` (
  `iid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`iid`,`name`),
  CONSTRAINT `genres_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
Genre = genresTable.genClass()

# No sample data here; things are created along with items
