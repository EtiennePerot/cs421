from library import sqlQuery

print sqlQuery("""
INSERT INTO has_languages (`iid`,`type`,`iso`) VALUES (
	(SELECT iid FROM video NATURAL JOIN items WHERE items.title = "An Apache's Gratitude"),
	'subtitled',
	(SELECT iso FROM languages WHERE english='French')
)
""")

print sqlQuery("""
UPDATE  members SET  balance = '0' WHERE  standing = 'good';
""")

print sqlQuery("""
DELETE FROM reserved_by WHERE reserved_by.to < CURRENT_TIMESTAMP
""")
