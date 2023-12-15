-- list all cities of california placed in our database
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = "California")
ORDER BY id;
