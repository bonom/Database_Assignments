-- Find the name and manufacturer of each beer that Fred likes.
SELECT *
FROM "Beers"
WHERE name IN (
    SELECT beer
    FROM "Likes"
    WHERE drinker = 'Fred'
);
