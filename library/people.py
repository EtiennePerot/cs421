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
	def changePassword(self, rawPassword, salt):
		self['password'] = _saltPassword(rawPassword, salt)
		self['salt'] = salt
	def asMember(self):
		return membersTable.findSingle(pnid=self['pnid'])
	def toMember(self, standing, balance, expiration):
		m = self.asMember()
		if m is None: # New member
			m = Member.createFromPerson(self, standing, balance, expiration)
		else: # Update existing member info if necessary
			m['standing'] = standing
			m['balance'] = balance
			m['expiration'] = expiration
			m.sync() # Will not do anything if no information has changed
		return m
	def asEmployee(self):
		return employeesTable.findSingle(pnid=self['pnid'])
	def toEmployee(self, role, salary, employed):
		e = self.asEmployee()
		if e is None: # New employee
			e = Employee.createFromPerson(self, role, salary, employed)
		else: # Update existing employee info if necessary
			e['role'] = role
			e['salary'] = salary
			e['employed'] = employed
			e.sync() # Will not do anything if no information has changed
		return e
peopleTable.bindClass(Person)

# Employees
employeesTable = dbTable("""CREATE TABLE `employees` (
  `pnid` int(10) unsigned NOT NULL,
  `role` varchar(255) DEFAULT NULL,
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
		return Employee.createFromPerson(p, role=role, salary=salary, employed=employed)
	@staticmethod
	def createFromPerson(person, role, salary, employed):
		return _rawEmployeeClass.create(pnid=person['pnid'], role=role, salary=salary, employed=employed)
employeesTable.bindClass(Employee)

# Members
membersTable = dbTable("""CREATE TABLE `members` (
  `pnid` int(11) unsigned NOT NULL,
  `standing` enum('good','bad') DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  `expiration` date DEFAULT NULL,
  PRIMARY KEY (`pnid`),
  CONSTRAINT `members_ibfk_1` FOREIGN KEY (`pnid`) REFERENCES `people` (`pnid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
_rawMemberClass = membersTable.genClass()
class Member(_rawMemberClass):
	@staticmethod
	def create(name, email, address, password, standing, balance, expiration):
		p = Person.create(name, email, address, password)
		return Member.createFromPerson(p, standing=standing, balance=balance, expiration=expiration)
	@staticmethod
	def createFromPerson(person, standing, balance, expiration):
		return _rawMemberClass.create(pnid=person['pnid'], standing=standing, balance=balance, expiration=expiration)
	def reserve(self, instance, fromDate, toDate, type):
		"""
			Sadly, due to "from" being a keyword in Python, we cannot use it as argument names.
			So the "from" has been renamed to "fromDate" in this function, and "to" has been renamed to "toDate" for consistency.
		"""
		return instance.reserve(member=self, fromDate=fromDate, toDate=toDate, type=type)
Member.standing_good = 'good'
Member.standing_bad = 'bad'
membersTable.bindClass(Member)

def generateRandomPeople(numPeople, printInfo=True):
	import people_generator
	people_generator.createPeople(numPeople, printInfo=printInfo)
