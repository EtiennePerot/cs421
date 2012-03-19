connect to cs421

echo Creating schema...

DROP TABLE people

DROP TABLE employees

CREATE TABLE people(pnid int NOT NULL, email varchar(255), address varchar(255), password CHAR(32), salt CHAR(32), name VARCHAR(255), PRIMARY KEY (pnid))

CREATE TABLE employees(pnid int NOT NULL, role varchar(255), salary double NOT NULL CHECK(salary >= 20000), employed date NOT NULL, PRIMARY KEY(pnid), FOREIGN KEY(pnid) REFERENCES people(pnid))

echo Inserting a few rows that match the constraint...

INSERT INTO people (pnid, email, address, password, salt, name) VALUES (1, 'bari-bertoldo@googlemail.com', '5036 Orange Avenue, Saxena', '8749bb8f1c227f31f8c5e2b61838a471', '734501cc1b22d85193d8a72ec4cefb3e', 'Bari Bertoldo')

INSERT INTO employees (pnid, role, salary, employed) VALUES (1, 'Librarian', 25070, '2009-05-28')

INSERT INTO people (pnid, email, address, password, salt, name) VALUES (2, 'pearliehendrikson@sogetthis.com', '8341 Mango Highway, Marconpolis', '730910f56181cb033d1ddc3ed8f7e2fa', '3e4dfaa2edee10186caa028ef1550071', 'Pearlie Hendrikson')

INSERT INTO employees (pnid, role, salary, employed) VALUES (2, 'Reviewer', 24325, '2009-11-27')

echo Attempting to insert a row that does not match the constraint... (the first INSERT will succeed, but not the second)

INSERT INTO people (pnid, email, address, password, salt, name) VALUES (3, 'marion.shankman@live.com', '8012 Pear Road, Bonkville', '8c6b2949e6aa4d72d6ffad99e5797762', '7f16ade9e2296a57fd9b9c07e988e09d', 'Marion Shankman')

INSERT INTO employees (pnid, role, salary, employed) VALUES (3, 'Janitor', 12500, '2010-09-16')

echo Attempting to update an existing row so that it does not match the constraint... (this should fail)

UPDATE employees SET salary = 15000 WHERE pnid = 2
