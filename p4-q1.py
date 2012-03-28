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


sqlQuery(

CREATE PROCEDURE procname(INOUT number INTEGER)
BEGIN

END


)



c.callproc(procname, args)
