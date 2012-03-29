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

#this one appears not to have syntax errors but is not functional
sqlQuery(

CREATE PROCEDURE addFines(IN fine INTEGER)
BEGIN
 DECLARE myPnid INT;
 DECLARE myDate DATE;
 DECLARE myPnidCopy INT DEFAULT 0;
REPEAT
 SET myPnid = 0; 
 SELECT pnid, `to` INTO @myPnid, @myDate 
  FROM members NATURAL JOIN reserved_by 
  WHERE type = "borrowed" AND `to` < CURRENT_DATE AND pnid != myPnidCopy LIMIT 1;
 SET myPnidCopy = @myPnid;
 UPDATE members
  SET balance = balance + fine*(CURRENT_DATE - myDate) WHERE pnid = myPnid;
UNTIL myPnid = 0
END REPEAT;
END

)

#still has syntax errors
sqlQuery(

CREATE PROCEDURE addFine(IN fine INTEGER)
BEGIN
thePnids = SELECT pnid FROM members WHERE pnid IN
 (SELECT pnid, `to` FROM members NATURAL JOIN reserved_by 
 WHERE type = "borrowed" AND `to` < CURRENT_DATE);
UPDATE members
 SET balance = balance + fine*(CURRENT_DATE - myDate) WHERE pnid IN thePnids;
END

)

# DECLARE standing  
# DECLARE myBalance 
# DECLARE myExpiration DATE;

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


c.callproc(addFines, args)
