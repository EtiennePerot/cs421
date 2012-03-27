#from library import sqlQuery #not using this

import pymysql

c = db.cursor()

#write procedure (temp name procname) here

c.callproc(procname, args)
