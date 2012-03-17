from library import sqlQuery

print sqlQuery("""
-- All actors that have acted in 10 movies or more
SELECT actors.name, COUNT(actors.name) FROM actors
	NATURAL JOIN has_actors
	GROUP BY actors.name
	HAVING COUNT(actors.name) >= 10
""")

print sqlQuery("""
-- Movies available in both english (spoken) and french (spoken) released in 1913
SELECT iid, title FROM items NATURAL JOIN video
	WHERE `date` >= '1913-01-01' AND `date` <= '1913-12-31'
	AND iid IN (
		SELECT iid FROM has_languages WHERE type = 'spoken' AND iso = 'en'
	) AND iid IN (
		SELECT iid FROM has_languages WHERE type = 'spoken' AND iso = 'fr'
	)
""")