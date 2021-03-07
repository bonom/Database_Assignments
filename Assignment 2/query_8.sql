-- List the bars that serve a beer that Joe likes.

SELECT DISTINCT bar
FROM "Sells"
NATURAL JOIN "Likes"
WHERE drinker = 'Joe'
