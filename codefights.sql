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

DROP FUNCTION IF EXISTS get_total;
CREATE FUNCTION get_total(items VARCHAR(45)) RETURNS INT DETERMINISTIC
BEGIN
    SET @newString = (SELECT items);
    SET @item = '-';
    -- SET @newString = (SELECT items FROM orders LIMIT 1);
    SET @price = 0; 
    WHILE (SELECT LENGTH(@newString)) > 0 DO
        IF (SELECT INSTR(@newString, ';'))>0 THEN
            SET @item = (SELECT SUBSTRING(@newString, 1, LOCATE(';', @newString, 1)-1));
            SET @newString = (SELECT substring(@newString, LOCATE(';', @newString, 1)+1));
        ELSE
            SET @item = (SELECT @newString);
            SET @newString = '';
        END IF;
        SET @price = @price + (SELECT price FROM item_prices WHERE id = CAST(@item AS UNSIGNED));                
    END WHILE;
    RETURN @price;
END