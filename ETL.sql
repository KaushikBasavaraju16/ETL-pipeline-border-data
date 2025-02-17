SELECT port_name, SUM(value) AS total_crossings
FROM border_crossings
GROUP BY port_name
ORDER BY total_crossings DESC
LIMIT 10;

SELECT State, Port_Name
FROM border_crossings 
WHERE Border = 'US-Canada Border'
AND State = 'New York'
Limit 10;