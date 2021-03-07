-- Find the beer(s) sold for the highest price.

SELECT DISTINCT beer
FROM "Sells"
WHERE price >= ALL (
    SELECT price
    FROM "Sells"
);
