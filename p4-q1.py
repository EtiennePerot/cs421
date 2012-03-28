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
REPEAT
 DECLARE number INTEGER DEFAULT 0; 
 SELECT pnid INTO number 
  FROM members NATURAL JOIN reserved_by 
  WHERE type = "borrowed" AND 'to' < CURRENT_DATE LIMIT 1;
 UPDATE members
  SET balance = balance + 1*(CURRENT_DATE - `to`) WHERE pnid = number;
UNTIL number = 0
END REPEAT;
END

#users with overdue items
#add fine to their accounts (DOES NOT QUITE WORK DUE TO STUPID ERROR)

#UPDATE members 
#SET balance = balance + 1*(CURRENT_DATE - `to`)
#  WHERE pnid =
#(SELECT pnid FROM members 
# WHERE pnid IN 
# (SELECT * FROM members NATURAL JOIN reserved_by 
#  WHERE type = "borrowed" AND 'to' < CURRENT_DATE));




)


#while exists record that matches
#set somevaraible to id of record that matches
#delete record with that id


c.callproc(procname, args)
