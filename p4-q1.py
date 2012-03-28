from library import sqlQuery 

import library import base

c = makeCursor()

#write procedure (temp name procname) here
#let's make a procedure that checks whether books have authors, publishers, etc. 
#it will also check for movies (writer, director, actors).
#it will search the appropriate database for each of these. 
#if it does not find the item, it will return a message for that particular item (did not find such and such)

#CREATE PROCEDURE procname(IN number INTEGER) ?
#LANGUAGE Python ?

#actually, this procedure will check for users with overdue items and add a fine to the accounts of users


sqlQuery(

CREATE PROCEDURE procname(IN fine INTEGER)
BEGIN

#users with overdue items
SELECT * FROM members NATURAL JOIN reserved_by WHERE type = "borrowed" AND 'to' < CURRENT_DATE LIMIT 30;
#add fine to their accounts
UPDATE members 
SET balance = balance + 1*(CURRENT_DATE - 'to')
  WHERE pnid IN 
(SELECT * FROM members NATURAL JOIN reserved_by WHERE type = "borrowed" AND 'to' < CURRENT_DATE);




END


)



c.callproc(procname, args)
