import sys
import pymysql as mysql
try:
	from config import dbConfig
except:
	print 'Please put a valid configuration file at library/config.py.'
	print 'Use library/config.template.py as base.'
	sys.exit(1)
try:
	conn = mysql.connect(**dbConfig)
except Exception, e:
	print 'Error while connecting to MySQL server:'
	print e
	sys.exit(1)
