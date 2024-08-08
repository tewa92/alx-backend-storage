-- lists the number of fans of each country ordered by the
-- number of fans in descending order
SELECT
    origin,
    SUM(fans) AS 'nb_fans'
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC
