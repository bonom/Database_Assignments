-- List the drinkers that frequent only bars that serve some beer that they like.
-- (Assume each drinker likes at least one beer and frequents at least one bar.)

SELECT f.drinker
FROM "Frequents" f
WHERE NOT EXISTS (
    -- frequents at least one that does not have something thet like
    SELECT *
    FROM "Frequents" y
    WHERE y.drinker = f.drinker AND NOT EXISTS (
        -- 1.lies and frequents
        SELECT *
        FROM "Sells" s
        NATURAL JOIN "Likes" l
        WHERE s.bar = y.bar AND l.drinker = y.drinker
    )
);
