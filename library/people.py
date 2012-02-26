import os, hashlib

from base import *

# Passwords are MD5 hashes computed as follows:
# satledPassword = md5(real password + 1337 + salt)
# Where salt is random hexadecimal characters

def _genSalt():
	return os.urandom(16).encode('hex')

def _saltPassword(password, salt):
	return hashlib.md5(password + salt).hexdigest()

# People
peopleTable = dbTable("""CREATE TABLE `people` (
  `pnid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `password` char(32) NOT NULL,
  `salt` char(32) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pnid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
_rawPersonClass = peopleTable.genClass()
class Person(_rawPersonClass):
	@staticmethod
	def create(name, email, address, password):
		salt = _genSalt()
		password = _saltPassword(password, salt)
		return _rawPersonClass.create(name=name, email=email, address=address, password=password, salt=salt)
	def checkPassword(self, password):
		return _saltPassword(password, self['salt']) == self['password']
peopleTable.bindClass(Person)

# Employees
employeesTable = dbTable("""CREATE TABLE `employees` (
  `pnid` int(10) unsigned NOT NULL,
  `role` enum('librarian') DEFAULT NULL,
  `salary` float DEFAULT NULL,
  `employed` date DEFAULT NULL,
  PRIMARY KEY (`pnid`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`pnid`) REFERENCES `people` (`pnid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
_rawEmployeeClass = employeesTable.genClass()
class Employee(_rawEmployeeClass):
	@staticmethod
	def create(name, email, address, password, role, salary, employed):
		p = Person.create(name, email, address, password)
		return _rawEmployeeClass.create(pnid=p['pnid'], role=role, salary=salary, employed=employed)
employeesTable.bindClass(Employee)

# Members
membersTable = dbTable("""CREATE TABLE `members` (
  `pnid` int(11) unsigned NOT NULL,
  `standing` enum('good','bad') DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  `expiration` datetime DEFAULT NULL,
  PRIMARY KEY (`pnid`),
  CONSTRAINT `members_ibfk_1` FOREIGN KEY (`pnid`) REFERENCES `people` (`pnid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
_rawMemberClass = membersTable.genClass()
class Member(_rawMemberClass):
	@staticmethod
	def create(name, email, address, password, standing, balance, expiration):
		p = Person.create(name, email, address, password)
		return _rawMemberClass.create(pnid=p['pnid'], standing=standing, balance=balance, expiration=expiration)
Member.standing_good = 'good'
Member.standing_bad = 'bad'
membersTable.bindClass(Member)
