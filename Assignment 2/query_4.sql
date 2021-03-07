-- Find those beers that are the unique beer by their manufacturer
SELECT name
FROM "Beers" f
WHERE NOT EXISTS (
    SELECT *
    FROM "Beers" s
    WHERE f.manf = s.manf AND f.name <> s.name
);
