-- Find the drinkers and beers such that:
--     the drinker likes the beer, and
--     the drinker frequents at least one bar that sells that beer.

(
    SELECT *
    FROM "Likes"
)
INTERSECT
(
    SELECT drinker, beer
    FROM "Sells"
    NATURAL JOIN "Frequents"
);
