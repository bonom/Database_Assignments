-- Find all the different prices charged for beers (no duplicates).

SELECT DISTINCT ROUND(price, 2)
FROM "Sells";
