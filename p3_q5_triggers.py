from library import sqlQuery

#data preperation queries
sqlQuery("""
    DROP TABLE `rental_history`
""")
sqlQuery("""
    CREATE TABLE rental_history (`iid` INT( 10 ) NOT NULL , `end_date` DATE NOT NULL , `type` ENUM(  'borrowed',  'reserved' ) NOT NULL) ENGINE = INNODB;
""")
sqlQuery("""
    DELETE FROM people WHERE pnid =1 or pnid=2
""")
sqlQuery("""
    TRUNCATE TABLE rental_history
""")
sqlQuery("""
    INSERT INTO people (pnid, email, address, password, salt, name)
    VALUES (1, 'yvanblanc@googlemail.com', '336 Park Avenue, Montreal, QC', '8749bb8f1c227f31f8c5e2b61838a471', '734501cc1b22d85193d8a72ec4cefb3e', 'Yvan Blanc')
""")
sqlQuery("""
    INSERT INTO members (pnid, standing, balance, expiration)
    VALUES (1, 'good', 0, '2013-2-28')
""")
sqlQuery("""
    INSERT INTO people (pnid, email, address, password, salt, name)
    VALUES (2, 'pearliehendrikson@sogetthis.com', '8341 Mango Highway, Marconpolis', '730910f56181cb033d1ddc3ed8f7e2fa', '3e4dfaa2edee10186caa028ef1550071', 'Pearlie Hendrikson')
""")
sqlQuery("""
    INSERT INTO members (pnid, standing, balance, expiration)
    VALUES (2, 'bad', 18, '2012-01-15')
""")
sqlQuery("""
    DELETE FROM items WHERE iid =1
""")
sqlQuery("""
    DELETE FROM instances WHERE instid =1
""")
sqlQuery("""
    INSERT INTO items (iid, title, date)
    VALUES (1, 'Hero Conquest', '2003-12-18')
""")
sqlQuery("""
    INSERT INTO instances (instid, iid)
    VALUES (1, 1)
""")

#Make triggers
sqlQuery("""
    DROP TRIGGER on_rental
""")
sqlQuery("""
    CREATE TRIGGER on_rental
    AFTER INSERT ON reserved_by
    FOR EACH ROW
    begin
        IF EXISTS(SELECT * from members where pnid = new.pnid and standing='bad')
            THEN UPDATE `Error: You cannot borrow/reserve items with a bad standing` SET x=0;
        END IF;
    End
""")
sqlQuery("""
    DROP TRIGGER item_returned
""")
sqlQuery("""
    CREATE TRIGGER item_returned
    AFTER DELETE ON reserved_by
    FOR EACH ROW
        INSERT INTO rental_history
        VALUES ( (Select iid from instances where instid=OLD.instid), CURRENT_TIMESTAMP , OLD.type);
""")

#query that doesn't activate item_returned and isn't blocked by on_rental
sqlQuery("""
    INSERT INTO  reserved_by (pnid ,instid ,`from` ,`to` ,type)VALUES (1,  1,  '2012-03-16',  '2012-03-29',  'borrowed')
""")
print sqlQuery("""
    SELECT * FROM reserved_by where pnid=1
""")
print sqlQuery("""
    SELECT * FROM rental_history
""")

#query that activates item_returned
sqlQuery("""
    DELETE FROM reserved_by WHERE instid=1
""")
print sqlQuery("""
    SELECT * FROM rental_history
""")

#query that gets blocked by on_rental
try:
    sqlQuery("""
        INSERT INTO  reserved_by (pnid ,instid ,`from` ,`to` ,type)VALUES (2,  1,  '2012-03-19',  '2012-04-02',  'borrowed')
    """)
except :
    print sqlQuery("""
        SELECT * FROM reserved_by WHERE pnid=2
    """)




