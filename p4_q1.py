from library import sqlQuery

from library import *

try: # Drop procedure if it exists
	sqlQuery('DROP PROCEDURE addFines')
except: # It didn't exist
	pass
# Now define it
sqlQuery("""
	CREATE PROCEDURE addFines(IN fine INTEGER) BEGIN
		DECLARE myPnid INT;
		DECLARE myDate DATE;
		DECLARE done INT DEFAULT FALSE;
		DECLARE pnids CURSOR FOR SELECT pnid, `to` FROM members NATURAL JOIN reserved_by WHERE type = "borrowed" AND `to` < CURRENT_DATE;
		DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
		OPEN pnids;
		read_loop: LOOP
			FETCH pnids INTO myPnid, myDate;
			IF done THEN
				LEAVE read_loop;
			END IF;
			IF EXISTS(SELECT 1 FROM employees WHERE pnid = myPnid) THEN
				UPDATE employees SET salary = salary - fine * (CURRENT_DATE - myDate) WHERE pnid = myPnid LIMIT 1;
			ELSE
				UPDATE members SET balance = balance + fine * (CURRENT_DATE - myDate) WHERE pnid = myPnid LIMIT 1;
			END IF;
		END LOOP;
		CLOSE pnids;
	END
""")


fine = None
while fine is None:
	try:
		fine = int(raw_input('How much is the fine? '))
	except:
		print 'Please enter an integer.'
		fine = None

transactionStart()
c = makeCursor()
c.callproc('addFines', [fine])
transactionCommit()
print 'Done.'
