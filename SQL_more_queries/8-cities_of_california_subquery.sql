-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- sorted in ascending order by cities.id
SELECT * FROM cities
WHERE state_id = @state_id
ORDER BY id ASC;