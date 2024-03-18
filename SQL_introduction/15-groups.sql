-- lists the number of records with the same score in the 2nd table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;