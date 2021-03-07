-- Find the bars that serve Miller and Bud at the same price.
SELECT DISTINCT f.bar
FROM "Sells" f, "Sells" s
WHERE f.bar = s.bar AND
    f.beer = 'Miller' AND s.beer = 'Bud' AND
    f.price = s.price;
