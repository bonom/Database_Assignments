-- List the drinkers that frequent at least one bar that serves a beer they like.

SELECT drinker
FROM (
    (
        SELECT *
        FROM "Likes"
    )
    INTERSECT
    (
        SELECT drinker, beer
        FROM "Sells"
        NATURAL JOIN "Frequents"
    )
) AS tmp;
