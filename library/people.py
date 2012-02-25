from base import *

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
