SELECT temp.email 
FROM (
    SELECT email, COUNT(email) AS ct
    FROM Person
    GROUP BY email
) temp WHERE temp.ct >= 2;