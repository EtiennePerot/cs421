import time
from library import *

setSqlVerbose(False)

iterations = 250

def benchmarkQuery(query, *indexes):
	for table, index in indexes:
		try: # Delete index if it exists
			sqlQuery('ALTER TABLE ' + sqlBackticks(table) + ' DROP INDEX ' + sqlBackticks(index))
		except: # Index probably didn't exist
			pass
	print 'Running query without indexes.'
	t = time.time()
	for i in xrange(iterations):
		sqlQuery(query)
	timeWithout = time.time() - t
	# Now add indexes
	for table, index in indexes:
		sqlQuery('ALTER TABLE ' + sqlBackticks(table) + ' ADD INDEX (' + sqlBackticks(index) + ')')
	print 'Running query with indexes.'
	t = time.time()
	for i in xrange(iterations):
		sqlQuery(query)
	timeWith = time.time() - t
	print timeWithout, timeWith

benchmarkQuery("""
-- All actors that have acted in 10 movies or more
-- Useful to know which actors are popular
SELECT actors.name, COUNT(actors.name) AS numberOfMovies FROM actors
	NATURAL JOIN has_actors
	GROUP BY actors.name
	HAVING COUNT(actors.name) >= 10
""", ('actors', 'name'))

benchmarkQuery("""
-- Movies available in both english (spoken) and french (spoken) released in 1913
-- Useful if we're looking for content in certain languages to share with a household where some people speak french and some english,
-- while looking for a particular period
SELECT iid, title FROM items NATURAL JOIN video
	WHERE `date` >= '1913-01-01' AND `date` <= '1913-12-31'
	AND iid IN (
		SELECT iid FROM has_languages WHERE type = 'spoken' AND iso = 'en'
	) AND iid IN (
		SELECT iid FROM has_languages WHERE type = 'spoken' AND iso = 'fr'
	)
""", ('items', 'date'), ('has_languages', 'iid'), ('has_languages', 'type'), ('has_languages', 'iso'))

benchmarkQuery("""
-- List members who have not given back their items before the end of their reservation date, and are already in bad standing.
-- Useful when wanting to see the list of people whose membership should probably be ended.
SELECT members.pnid, name, email, balance FROM members NATURAL JOIN people WHERE standing = 'bad' AND EXISTS (
	SELECT 1 FROM reserved_by
	WHERE reserved_by.pnid = members.pnid
	AND `to` < CURRENT_DATE
	LIMIT 1 -- Only need one record to check existence
)
""", ('members', 'standing'), ('reserved_by', 'pnid'), ('reserved_by', 'to'))
