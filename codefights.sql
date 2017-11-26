/*Please add ; after each select statement*/
CREATE PROCEDURE recentHires()
BEGIN
    SELECT name FROM (
    SELECT name
    FROM pr_department a 
    INNER JOIN 
        (SELECT id FROM pr_department ORDER BY date_joined DESC LIMIT 5) 
    b ON a.id = b.id ORDER BY name) A
    UNION
    SELECT name FROM (
	SELECT name
    FROM it_department a 
    INNER JOIN 
        (SELECT id FROM it_department ORDER BY date_joined DESC LIMIT 5) 
    b ON a.id = b.id ORDER BY name) B
    UNION
    SELECT name FROM (
	SELECT name
    FROM sales_department a 
    INNER JOIN 
        (SELECT id FROM sales_department ORDER BY date_joined DESC LIMIT 5) 
    b ON a.id = b.id ORDER BY name) C
    ;
END