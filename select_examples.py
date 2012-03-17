from library import sqlQuery

print sqlQuery("""

SELECT actors.name, COUNT(*) FROM actors
NATURAL JOIN has_actors
GROUP BY actors.name

""")