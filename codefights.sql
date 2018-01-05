/*Please add ; after each SELECT statement*/
-- CREATE PROCEDURE recentHires()
-- BEGIN
    -- SELECT name FROM (
    -- SELECT name
    -- FROM pr_department a 
    -- INNER JOIN 
--         (SELECT id FROM pr_department ORDER BY date_joined DESC LIMIT 5) 
--     b ON a.id = b.id ORDER BY name) A
--     UNION
--     SELECT name FROM (
-- 	SELECT name
--     FROM it_department a 
--     INNER JOIN 
--         (SELECT id FROM it_department ORDER BY date_joined DESC LIMIT 5) 
--     b ON a.id = b.id ORDER BY name) B
--     UNION
--     SELECT name FROM (
-- 	SELECT name
--     FROM sales_department a 
--     INNER JOIN 
--         (SELECT id FROM sales_department ORDER BY date_joined DESC LIMIT 5) 
--     b ON a.id = b.id ORDER BY name) C
--     ;
-- END

-- DROP FUNCTION IF EXISTS get_total;
-- CREATE FUNCTION get_total(items VARCHAR(45)) RETURNS INT DETERMINISTIC
-- BEGIN
--     SET @newString = (SELECT items);
--     SET @item = '-';
--     -- SET @newString = (SELECT items FROM orders LIMIT 1);
--     SET @price = 0; 
--     WHILE (SELECT LENGTH(@newString)) > 0 DO
--         IF (SELECT INSTR(@newString, ';'))>0 THEN
--             SET @item = (SELECT SUBSTRING(@newString, 1, LOCATE(';', @newString, 1)-1));
--             SET @newString = (SELECT substring(@newString, LOCATE(';', @newString, 1)+1));
--         ELSE
--             SET @item = (SELECT @newString);
--             SET @newString = '';
--         END IF;
--         SET @price = @price + (SELECT price FROM item_prices WHERE id = CAST(@item  UNSIGNED));                
--     END WHILE;
--     RETURN @price;
-- END

<<<<<<< HEAD
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
=======
-- SELECT pack.id  id, MIN(pack.length * pack.width * pack.height)  box_dim
-- FROM (
--     SELECT id, package_type, length, width, height
--     FROM gifts gift INNER JOIN packages package
--     ON gift.length <= package.length AND gift.width <= package.width and gift.height <= package.height
--     ) pack
-- GROUP BY pack.id



-- DROP TABLE IF EXISTS caracteres;
--      CREATE temporary TABLE caracteres(
--           cadena varchar(255) default null,
--           letra varchar(55) default null,
--           cuenta int default null
--           );

--      INSERT INTO temp
--         SELECT str, 'a', LENGTH(str) - LENGTH(REPLACE(str, 'a', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'b', LENGTH(str) - LENGTH(REPLACE(str, 'b', ''))  cuenta FROM strs
--           UNION
--                SELECT str, 'c', LENGTH(str) - LENGTH(REPLACE(str, 'c', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'd', LENGTH(str) - LENGTH(REPLACE(str, 'd', ''))  cuenta FROM strs
--           UNION 
--         SELECT str, 'e', LENGTH(str) - LENGTH(REPLACE(str, 'e', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'f', LENGTH(str) - LENGTH(REPLACE(str, 'f', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'g', LENGTH(str) - LENGTH(REPLACE(str, 'g', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'h', LENGTH(str) - LENGTH(REPLACE(str, 'h', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'i', LENGTH(str) - LENGTH(REPLACE(str, 'i', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'j', LENGTH(str) - LENGTH(REPLACE(str, 'j', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'k', LENGTH(str) - LENGTH(REPLACE(str, 'k', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'l', LENGTH(str) - LENGTH(REPLACE(str, 'l', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'm', LENGTH(str) - LENGTH(REPLACE(str, 'm', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'n', LENGTH(str) - LENGTH(REPLACE(str, 'n', ''))  cuenta FROM strs          UNION
--         SELECT str, 'o', LENGTH(str) - LENGTH(REPLACE(str, 'o', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'p', LENGTH(str) - LENGTH(REPLACE(str, 'p', ''))  cuenta FROM strs          UNION
--         SELECT str, 'q', LENGTH(str) - LENGTH(REPLACE(str, 'q', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 'r', LENGTH(str) - LENGTH(REPLACE(str, 'r', ''))  cuenta FROM strs
--           UNION
--         SELECT str, 's', LENGTH(str) - LENGTH(REPLACE(str, 's', ''))  cuenta FROM strs
--         UNION
--         SELECT str, 't', LENGTH(str) - LENGTH(REPLACE(str, 't', ''))  cuenta FROM strs
--       UNION
--         SELECT str, 'u', LENGTH(str) - LENGTH(REPLACE(str, 'u', ''))  cuenta FROM strs
--   UNION
--         SELECT str, 'v', LENGTH(str) - LENGTH(REPLACE(str, 'v', ''))  cuenta FROM strs
--   UNION
--         SELECT str, 'w', LENGTH(str) - LENGTH(REPLACE(str, 'w', ''))  cuenta FROM strs
--   UNION
--         SELECT str, 'x', LENGTH(str) - LENGTH(REPLACE(str, 'x', ''))  cuenta FROM strs
--   UNION
--         SELECT str, 'y', LENGTH(str) - LENGTH(REPLACE(str, 'y', ''))  cuenta FROM strs
--   UNION
--         SELECT str, 'z', LENGTH(str) - LENGTH(REPLACE(str, 'z', ''))  cuenta FROM strs
-- ;

--     SELECT total.letra, total.total, occurrences.occurrence  occurrence, max_occurreces.max_occurrence max_occurrence, max_occurrences_reached.max_occurence_reached  max_occurrence_reached
--     FROM (
--       SELECT letra, SUM(cuenta) total
--        FROM caracteres
--        GROUP BY letra
--        HAVING SUM(cuenta) >= 1
--     ) total
--     JOIN (
--       SELECT DISTINCT letra, COUNT(letra) occurrence
--        FROM caracteres
--        WHERE cuenta > 0
--        GROUP BY letra
--     ) occurrences
--     ON occurrences.letra = total.letra
--     JOIN (
--       SELECT letra, MAX(cuenta) max_occurence
--        FROM caracteres 
--        WHERE cuenta > 0
--        GROUP BY letra
--     ) max_occurrences 
--     on total.letra = max_occurrences.letra
--     JOIN (
--        SELECT a.letra, COUNT(*) max_occurence_reached
--          FROM (
--            SELECT b.letra, b.cuenta
--            FROM caracteres b
--              JOIN (
--                SELECT letra, MAX(cuenta)  max_occurence
--                FROM caracteres 
--                WHERE cuenta > 0
--                GROUP BY letra
--              ) c 
--            ON c.letra = b.letra AND c.max_occurence = b.cuenta
--        ) a
--        GROUP BY a.letra
--     ) max_occurrence_reached 
--     ON total.letra = max_occurrences_reached.letra
--     ORDER BY total.letra;



--     SET @rowid = 0;

--     SELECT a.dep_name, 
--     CASE WHEN a.emp_number IS NULL THEN 0 ELSE a.emp_number END as emp_number, 
--     CASE WHEN a.total_salary IS NULL THEN 0 ELSE a.total_salary END as total_salary
--     FROM (
--       SELECT b.*, @rowid := @rowid + 1 as rowid
--       FROM (
--         SELECT d.name dep_name,
--                COUNT(e.department) emp_number, 
--                SUM(e.salary) total_salary
--           FROM Employee e
--         RIGHT JOIN Department d
--                 ON e.department = d.id
--           GROUP by d.id
--           HAVING COUNT(e.department) < 6
--           ORDER BY sum(e.salary) desc, emp_number desc, d.id asc 
--           ) b
--         ) a  
--    where a.rowid % 2 != 0;


-- DECLARE done BOOLEAN DEFAULT 0;
-- DECLARE dname VARCHAR(255) DEFAULT "";
-- DECLARE ddate DATE;
-- DECLARE dmiles INT DEFAULT 0;
-- DECLARE current_dn VARCHAR(255) DEFAULT "";

-- DECLARE cur CURSOR FOR
--   SELECT driver_name, date, miles_logged 
--   FROM inspections
--   ORDER BY driver_name, date;
-- DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

-- DROP TABLE IF EXISTS summary;
-- CREATE TABLE summary (str VARCHAR(255));
-- SET @total := (SELECT SUM(miles_logged) FROM inspections);
-- INSERT INTO summary VALUES (CONCAT(' Total miles driven by all drivers combined: ', @total));

-- OPEN cur;
-- get_driver: LOOP
-- FETCH cur INTO dname, ddate, dmiles;
--   IF done = 1 THEN 
--     LEAVE get_driver;
--   END IF;
--   IF current_dn <> dname THEN
--     SET @sum := (SELECT SUM(miles_logged) FROM inspections where driver_name=dname);
--     SET @ct := (SELECT count(*) FROM inspections where driver_name=dname);
--     INSERT INTO summary values (CONCAT(" Name: ",dname,";"," number of inspections: ", @ct,";" , " miles driven: ", @sum));
--     SET current_dn := dname;
--   END IF;
--   INSERT INTO summary VALUES(CONCAT("  date: ", ddate, "; miles covered: ", dmiles));
-- END LOOP get_driver;
-- CLOSE cur;

-- SELECT str as summary FROM summary;

--    SELECT
--         ELT(w, name_naughts, name_crosses) name,
--         SUM((x=w)*2 + (x=3)) points,
--         SUM(1) played,
--         SUM(x=w) won,
--         SUM(x=3) draw,
--         SUM(x=3-d) lost
--     FROM
--         (
--             SELECT name_naughts, name_crosses, IF (board RLIKE '^(...)*XXX|X..(X|.X.)..X|^..X.X.X', 2, LENGTH(REPLACE(board, '.', ''))%2*2+1) x
--               FROM results
--         ) A,
--         (
--         SELECT 1 w 
--         UNION 
--         SELECT 2
--         ) B
--     GROUP BY 1
--     ORDER BY 2 DESC, 3, 5, 1
--     ;

/*EXTREME LONG SOLUTION*/



/*Please add ; after each select statement*/
CREATE PROCEDURE tictactoeTournament()
BEGIN
    SET @xwin := ('(XXX[XO\.]{6})|([XO\.]{3}XXX[XO\.]{3})|([XO\.]{6}XXX)|(X[XO\.]{2}X[XO\.]{2}X[XO\.]{2})|([XO\.]X[XO\.][XO\.]X[XO\.][XO\.]X[XO\.])|([XO\.]{2}X[XO\.]{2}X[XO\.]{2}X)|(X[XO\.]{3}X[XO\.]{3}X)|([XO\.]{2}X[XO\.]X[XO\.]X[XO\.]{2})');

    SET @owin = ('(OOO[XO\.]{6})|([XO\.]{3}OOO[XO\.]{3})|([XO\.]{6}OOO)|(O[XO\.]{2}O[XO\.]{2}O[XO\.]{2})|([XO\.]O[XO\.][XO\.]O[XO\.][XO\.]O[XO\.])|([XO\.]{2}O[XO\.]{2}O[XO\.]{2}O)|(O[XO\.]{3}O[XO\.]{3}O)|([XO\.]{2}O[XO\.]O[XO\.]O[XO\.]{2})');

SELECT name, (SUM(xwon) + SUM(owon)) *2 + SUM(draw) as points, COUNT(name) as played, SUM(xwon) + SUM(owon) as won, SUM(draw) as draw, COUNT(name) - SUM(xwon)  - SUM(owon) - SUM(draw) as lost FROM
(
SELECT name_crosses as name, xwon, owon, draw FROM 
(
SELECT *, board REGEXP @xwin as xwon, board REGEXP @owin as owon, board REGEXP @owin = 0 AND board REGEXP @xwin = 0 as draw from results
) as a
WHERE xwon = 1

UNION ALL

SELECT name_naughts as name, xwon, owon, draw FROM 
(
SELECT *, board REGEXP @xwin as xwon, board REGEXP @owin as owon, board REGEXP @owin = 0 AND board REGEXP @xwin = 0 as draw from results
) as b
WHERE owon = 1

UNION ALL

SELECT name_naughts as name, xwon, owon, draw FROM 
(
SELECT *, board REGEXP @xwin as xwon, board REGEXP @owin as owon, board REGEXP @owin = 0 AND board REGEXP @xwin = 0 as draw from results
) as c
WHERE draw = 1

UNION ALL

SELECT name_crosses as name, xwon, owon, draw FROM 
(
SELECT *, board REGEXP @xwin as xwon, board REGEXP @owin as owon, board REGEXP @owin = 0 AND board REGEXP @xwin = 0 as draw from results
) as d
WHERE draw = 1

UNION ALL

SELECT name_crosses as name, 0 as xwon, 0 as owon, 0 as draw FROM 
(
SELECT *, board REGEXP @xwin as xwon, board REGEXP @owin as owon, board REGEXP @owin = 0 AND board REGEXP @xwin = 0 as draw from results
) as e
WHERE owon = 1

UNION ALL

<<<<<<< HEAD
SELECT name_naughts as name, 0 as xwon, 0 as owon, 0 as draw FROM 
(
SELECT *, board REGEXP @xwin as xwon, board REGEXP @owin as owon, board REGEXP @owin = 0 AND board REGEXP @xwin = 0 as draw from results
) as f
WHERE xwon = 1
) as h
GROUP BY name
ORDER BY points DESC, played ASC, won DESC, name ASC;
=======
>>>>>>> 4586b60474cee1ff6e3e5156bc8e1f75b385f37c
>>>>>>> 94b61f49243158110c7ceaefcf57f1764a0bd49e
