from library import sqlQuery

print sqlQuery("""
    insert into has_languages(`iid`,`type`,`iso`)Values((select iid from video natural join items where items.title= "An Apache's Gratitude"),'subtitled',(select iso from languages where english = 'French'));
    UPDATE  members SET  balance =  '0' WHERE  standing ='good';
    DELETE FROM reserved_by WHERE reserved_by.to < CURRENT_TIMESTAMP;
""")

