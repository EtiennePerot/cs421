from library import sqlQuery

print sqlQuery("""
-- All actors that have acted in 10 movies or more
-- Useful to know which actors are popular
SELECT actors.name, COUNT(actors.name) AS numberOfMovies FROM actors
	NATURAL JOIN has_actors
	GROUP BY actors.name
	HAVING COUNT(actors.name) >= 10
""")

print sqlQuery("""
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
""")

print sqlQuery("""
-- List members who have not given back their items before the end of their reservation date, and are already in bad standing.
-- Useful when wanting to see the list of people whose membership should probably be ended.
SELECT members.pnid, name, email, balance FROM members NATURAL JOIN people WHERE standing = 'bad' AND EXISTS (
	SELECT 1 FROM reserved_by
	WHERE reserved_by.pnid = members.pnid
	AND `to` < CURRENT_DATE
	LIMIT 1 -- Only need one record to check existence
)
""")

print sqlQuery("""
-- Audio albums that have a total duration of more than 10 minutes, combined with videos that are between 8 and 12 minutes in length, ordered by total duration
-- Useful if we have "x" minutes of time and want to borrow something that is guaranteed to fill that time gap, no matter what type of media it is
(
	SELECT
		'audio' AS `type`,
		title,
		ROUND(longAlbums.totalAlbumDuration / 60) AS totalDuration
	FROM items NATURAL JOIN (
		SELECT audio.iid, SUM(songs.duration) AS totalAlbumDuration
		FROM audio NATURAL JOIN songs
		GROUP BY audio.iid
		HAVING SUM(songs.duration) > 10 * 60
	) AS longAlbums
) UNION (
	SELECT
	'video' as `type`,
	title,
	duration AS totalDuration
	FROM video NATURAL JOIN items
	WHERE duration >= 10 AND duration <= 12
) ORDER BY totalDuration
""")