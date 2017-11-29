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

/*Please add ; after each select statement*/
CREATE PROCEDURE bugsInComponent()
BEGIN    

        SELECT b.title bug_title, c.title component_title, 
            (SELECT COUNT(component_id) 
               FROM BugComponent e INNER JOIN Component f 
               ON e.component_id = f.id WHERE f.title = c.title) bugs_in_component
        FROM BugComponent a INNER JOIN Bug b
          ON a.bug_num = b.num INNER JOIN Component c
          ON a.component_id = c.id  INNER JOIN (
            SELECT bug_num, max_bug_num FROM BugComponent a INNER JOIN ( 
            SELECT MAX(bn.bug_nums) max_bug_num 
            FROM (SELECT bug_num, COUNT(bug_num) bug_nums FROM BugComponent GROUP BY bug_num) bn
            ) b
            GROUP BY bug_num
            HAVING COUNT(bug_num) = max_bug_num
            ) d ON b.num = d.bug_num
        ORDER BY bugs_in_component DESC, a.component_id, a.bug_num
        ;

END