from base import *

actorsTable = dbTable("""CREATE TABLE `actors` (
 `aid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Actor ID',
 `name` varchar(255) NOT NULL,
 PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
Actor = actorsTable.genClass()

def actorByName(name):
	return actorsTable.findSingle(name=name)

hasActorsTable = dbTable("""CREATE TABLE `has_actors` (
 `iid` int(11) unsigned NOT NULL,
 `aid` int(11) unsigned NOT NULL,
 PRIMARY KEY (`iid`,`aid`),
 KEY `aid` (`aid`),
 CONSTRAINT `has_actors_ibfk_2` FOREIGN KEY (`aid`) REFERENCES `actors` (`aid`) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT `has_actors_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
HasActor = hasActorsTable.genClass()
