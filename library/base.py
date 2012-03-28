import sys
import re
import pymysql as mysql
from pymysql import cursors

class curry:
	def __init__(self, func, *args, **kwargs):
		self.func = func
		self.pending = args[:]
		self.kwargs = kwargs
	def __call__(self, *args, **kwargs):
		if kwargs and self.kwargs:
			kw = self.kwargs.copy()
			kw.update(kwargs)
		else:
			kw = kwargs or self.kwargs
		return self.func(*(self.pending + args), **kw)

try:
	from config import dbConfig
except:
	print 'Please put a valid configuration file at library/config.py.'
	print 'Use library/config.template.py as base.'
	sys.exit(1)
try:
	conn = mysql.connect(**dbConfig)
except Exception, e:
	print 'Error while connecting to MySQL server:'
	print e
	sys.exit(1)

def _sqlBackticks(s):
	if type(s) is type([]):
		return ', '.join([_sqlBackticks(x) for x in s])
	if isinstance(s, dbTable):
		return _sqlBackticks(s.getName())
	return '`' + s.replace('\\', '\\\\').replace('`', '\\`') + '`'

def _sqlColumnClause(params, suffix=''):
	if len(suffix):
		return ' AND '.join([_sqlBackticks(k[:-len(suffix)]) + ' = %(' + k[:-len(suffix)] + suffix + ')s' for k in params])
	return ' AND '.join([_sqlBackticks(k) + ' = %(' + k + ')s' for k in params])

def _sqlValuesClause(params):
	return ', '.join(['%(' + k + ')s' for k in params])

class libraryCursor(cursors.Cursor):
	def execute(self, query, args=None):
		result = super(libraryCursor, self).execute(query, args)
		if self.description:
			self._fields = [unicode(field[0]) for field in self.description]
		return result
	def __repr__(self):
		return str(self)
	def __str__(self):
		return unicode(self).encode('utf8')
	def __unicode__(self):
		if not self.description:
			return u'(No results to display)'
		results = self.fetchall()
		rows = []
		maxColSize = [len(f) for f in self._fields]
		for r in results:
			row = []
			for f in xrange(len(r)):
				val = unicode(r[f])
				maxColSize[f] = max(maxColSize[f], len(val))
				row.append(val)
			rows.append(row)
		fieldsHeader = []
		fieldsLine = []
		for f in xrange(len(self._fields)):
			field = self._fields[f] + u' ' * (maxColSize[f] - len(self._fields[f]))
			fieldsHeader.append(field)
			fieldsLine.append(u'-' * len(field))
		resultString = [u' ' + u' | '.join(fieldsHeader) + u' ', u'-' + u'-+-'.join(fieldsLine) + u'-']
		for r in rows:
			s = []
			for f in xrange(len(r)):
				s.append(r[f] + u' ' * (maxColSize[f] - len(r[f])))
			resultString.append(u' ' + u' | '.join(s) + u' ')
		return u'\n'.join(resultString)

#added for p4
def makeCursor():
	return conn.cursor()

def _sqlQuery(query, _cursor=None, asDict=False, **params):
	if asDict:
		cursor = conn.cursor(cursors.DictCursor)
	elif _cursor is not None:
		cursor = conn.cursor(_cursor)
	else:
		cursor = conn.cursor(libraryCursor)
	print '~ Executing query:'
	print query
	if len(params):
		print '~ With params:', params
	cursor.execute(query, params)
	conn.commit()
	return cursor

# Public interface; may eventually not be a direct pointer to the private interface
sqlQuery = _sqlQuery

class dbTable(object):
	findBackString = re.compile('`([^`]+)`')
	def __init__(self, sql):
		self._sqlCreate = sql
		self._name = None
		self._autoIncrement = None
		self._primary = []
		self._fields = []
		for s in sql.split('\n'):
			for backString in dbTable.findBackString.finditer(s):
				backString = backString.group(1)
				if 'CREATE TABLE' in s:
					self._name = backString
				elif 'PRIMARY KEY' in s:
					if s not in self._primary:
						self._primary.append(backString)
				elif 'KEY' not in s and 'CONSTRAINT' not in s and backString not in self._fields:
					self._fields.append(backString)
					if 'AUTO_INCREMENT' in s:
						self._autoIncrement = backString
		if self._name is None:
			raise Exception('Couldn\'t parse create table SQL statement.')
		self._recordClass = None
	def __str__(self):
		return unicode(self).encode('utf8')
	def __unicode__(self):
		return unicode(self._name)
	def create(self):
		_sqlQuery(self._sqlCreate).close()
	def drop(self):
		_sqlQuery('DROP TABLE ' + _sqlBackticks(self._name)).close()
	def _paramsIntersect(self, params):
		filteredParams = {}
		activeFields = []
		for f in self._fields:
			if f in params:
				if isinstance(params[f], _dbInstance) and len(params[f].getTable()._primary) == 1:
					filteredParams[f] = params[f][params[f].getTable()._primary[0]]
				else:
					filteredParams[f] = params[f]
				activeFields.append(f)
		return activeFields, filteredParams
	def getName(self):
		return self._name
	def _new(self, params):
		activeFields, filteredParams = self._paramsIntersect(params)
		q = _sqlQuery(
			'INSERT INTO ' + _sqlBackticks(self._name) + '(' + _sqlBackticks(activeFields) + ') VALUES(' + _sqlValuesClause(activeFields) + ')',
			**filteredParams
		)
		try:
			lastRowId = q.lastrowid
		except:
			lastRowId = None
		q.close()
		objParams = filteredParams.copy()
		if len(activeFields) != len(self._fields) and self._autoIncrement is not None and lastRowId is not None:
			objParams[self._autoIncrement] = q.lastrowid
			activeFields.append(self._autoIncrement)
		if len(activeFields) != len(self._fields):
			# We're still missing information
			otherFields = []
			for f in self._fields:
				if f not in activeFields:
					otherFields.append(f)
			q2 = _sqlQuery(
				'SELECT ' + _sqlBackticks(otherFields) + ' FROM ' + _sqlBackticks(self._name) + ' WHERE ' + _sqlColumnClause(filteredParams) + ' LIMIT 1',
				**filteredParams
			)
			row = q2.fetchone()
			if row is None:
				raise Exception('Error while inserting new record; couldn\'t find the inserted record.')
			for i in xrange(len(otherFields)):
				objParams[otherFields[i]] = row[i]
		return self._getRecordClass()(**objParams)
	def _objectGetParams(self, paramList, obj, old=False, suffix=''):
		params = {}
		for p in paramList:
			if old:
				params[p + suffix] = obj._oldFields[p]
			else:
				params[p + suffix] = obj[p]
		return params
	def _objectGetAllParams(self, obj, old=False, suffix=''):
		return self._objectGetParams(self._fields, obj, old=old, suffix=suffix)
	def _objectGetPrimaryParams(self, obj, old=False, suffix=''):
		return self._objectGetParams(self._primary, obj, old=old, suffix=suffix)
	def _objectExists(self, obj):
		params = self._objectGetPrimaryParams(obj)
		q = _sqlQuery(
			'SELECT EXISTS(SELECT 1 FROM ' + _sqlBackticks(self._name) + ' WHERE ' + _sqlColumnClause(params) + ' LIMIT 1)',
			**params
		)
		result = bool(q.fetchone()[0])
		q.close()
		return result
	def _objectUpdate(self, obj):
		oldPrimary = self._objectGetPrimaryParams(obj, old=True,  suffix='_w')
		oldAll     = self._objectGetAllParams(obj, old=True, suffix='_u')
		newAll     = self._objectGetAllParams(obj, old=False, suffix='_u')
		allParams = {}
		allParams.update(oldPrimary)
		allParams.update(newAll)
		newFiltered = {}
		for p in newAll:
			if p not in oldAll or newAll[p] != oldAll[p]:
				newFiltered[p] = newAll[p]
		q = _sqlQuery(
			'UPDATE ' + _sqlBackticks(self._name) + ' SET ' + _sqlColumnClause(newFiltered, suffix='_u') + ' WHERE ' + _sqlColumnClause(oldPrimary, suffix='_w') + ' LIMIT 1',
			**allParams
		)
		q.close()
	def _objectDelete(self, obj):
		params = self._objectGetPrimaryParams(obj)
		_sqlQuery(
			'DELETE FROM ' + _sqlBackticks(self._name) + ' WHERE ' + _sqlColumnClause(params) + ' LIMIT 1',
			**params
		).close()
	def bindClass(self, newClass):
		self._recordClass = newClass
	def fromResults(self, results):
		if type(results) in (type([]), type(())):
			return [self.fromResults(x) for x in results]
		return self._getRecordClass()(**results)
	def genClass(self):
		table = self
		class newClass(_dbInstance):
			@staticmethod
			def create(**params):
				return table._new(params)
			def __init__(self, **fields):
				_dbInstance.__init__(self, table, **fields)
		return newClass
	def _getRecordClass(self):
		if self._recordClass is None:
			self._recordClass = self.genClass()
		return self._recordClass
	def findSingle(self, **params):
		result = self.find(limit=1, **params)
		if not len(result):
			return None
		return result[0]
	def getAll(self):
		return self.find()
	def find(self, limit=None, **params):
		activeFields, params = self._paramsIntersect(params)
		sqlWhere = ''
		if len(activeFields):
			sqlWhere = ' WHERE ' + _sqlColumnClause(activeFields)
		limitString = ''
		if limit is not None and type(limit) is type(0) and limit > 0:
			limitString = ' LIMIT ' + str(limit)
		q = _sqlQuery(
			'SELECT ' + _sqlBackticks(self._fields) + ' FROM ' + _sqlBackticks(self._name) + sqlWhere + limitString,
			_cursor = cursors.DictCursor,
			**params
		)
		results = q.fetchall()
		if results is None:
			return []
		objectResults = []
		for r in results:
			objectResults.append(self._getRecordClass()(**r))
		return objectResults

class _dbInstance(object):
	def __init__(self, table=None, **fields):
		self._table = table
		self._fields = fields.copy()
		self._oldFields = fields.copy()
		self._upToDate = True
	def __getitem__(self, key):
		if key not in self._fields:
			return None
		return self._fields[key]
	def __setitem__(self, key, val):
		if key in self._fields and self._fields[key] == val:
			return # No need to change anything
		self._fields[key] = val
		self._upToDate = False
	def __delitem__(self, key):
		if key in self._fields:
			del self._fields[key]
	def __str__(self):
		return unicode(self).encode('utf8')
	def __unicode__(self):
		s = u', '.join([unicode(k) + u'=' + unicode(v) for k, v in self._fields.items()])
		return unicode(self._table) + u'(' + s + u')'
	def getTable(self):
		return self._table
	def delete(self):
		return self._table._objectDelete(self)
	def sync(self):
		if not self._upToDate:
			self._table._objectUpdate(self)
			self._oldFields = self._fields.copy()
			self._upToDate = True
