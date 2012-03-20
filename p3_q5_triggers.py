from library import sqlQuery

print sqlQuery("""
    CREATE TRIGGER item_returned AFTER DELETE ON reserved_by FOR EACH ROW INSERT INTO rental_history VALUES ( (Select iid from instances where instid=OLD.instid), CURRENT_TIMESTAMP , OLD.type);
""")
print sqlQuery("""
    CREATE Trigger on_rental AFTER INSERT ON reserved_by FOR EACH ROW begin IF EXISTS(SELECT * from members where pnid = new.pnid and standing='bad') THEN DELETE FROM reserved_by WHERE pnid = new.pnid ;END IF; End
""")
