import sys
import pymysql as mysql
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
	return '`' + s.replace('\\', '\\\\').replace('`', '\\`') + '`'

def _sqlColumnClause(params, suffix=''):
	if len(suffix):
		return ' AND '.join([_sqlBackticks(k[:-len(suffix)]) + ' = %(' + k[:-len(suffix)] + suffix + ')s' for k in params])
	return ' AND '.join([_sqlBackticks(k) + ' = %(' + k + ')s' for k in params])

def _sqlValuesClause(params):
	return ', '.join(['%(' + k + ')s' for k in params])

def _sqlQuery(query, **params):
	cursor = conn.cursor()
	print '~ Executing query:'
	print query
	print '~ With params:', params
	cursor.execute(query, params)
	conn.commit()
	return cursor

class _dbTable(object):
	def __init__(self, name, *fields):
		"""
			Notation:
			_dbTable('tablename', 'field1', 'field2, ..., '*primarykey1', '*primarykey2', ...)
		"""
		self._name = name
		self._primary = []
		self._fields = []
		for f in fields:
			if f[0] == '*':
				self._primary.append(f[1:])
				self._fields.append(f[1:])
			else:
				self._fields.append(f)
	def _new(self, params):
		filteredParams = {}
		activeFields = []
		for f in self._fields:
			if f in params:
				filteredParams[f] = params[f]
				activeFields.append(f)
		q = _sqlQuery(
			'INSERT INTO ' + _sqlBackticks(self._name) + '(' + _sqlBackticks(activeFields) + ') VALUES(' + _sqlValuesClause(activeFields) + ')',
			**filteredParams
		)
		q.close()
		objParams = filteredParams.copy()
		if len(activeFields) != len(self._fields):
			# Got to find out the rest of the data we inserted
			otherFields = []
			for f in self._fields:
				if f not in activeFields:
					otherFields.append(f)
			q2 = _sqlQuery(
				'SELECT ' + _sqlBackticks(otherFields) + ' FROM ' + _sqlBackticks(self._name) + ' WHERE ' + _sqlColumnClause(filteredParams) + ' LIMIT 1',
				**filteredParams
			)
			row = q2.fetchone()
			i = 0
			for f in otherFields:
				objParams[f] = row[i]
				i += 1
		return objParams
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
		newAll     =     self._objectGetAllParams(obj, old=False, suffix='_u')
		allParams = {}
		allParams.update(oldPrimary)
		allParams.update(newAll)
		q = _sqlQuery(
			'UPDATE ' + _sqlBackticks(self._name) + ' SET ' + _sqlColumnClause(newAll, suffix='_u') + ' WHERE ' + _sqlColumnClause(oldPrimary, suffix='_w') + ' LIMIT 1',
			**allParams
		)
		q.close()
	def _objectDelete(self, obj):
		params = self._objectGetPrimaryParams(obj)
		_sqlQuery(
			'DELETE FROM ' + _sqlBackticks(self._name) + ' WHERE ' + _sqlColumnClause(params) + ' LIMIT 1',
			**params
		).close()
	def genClass(self):
		table = self
		class newClass(_dbInstance):
			@staticmethod
			def create(**params):
				return newClass(**table._new(params))
			def __init__(self, **fields):
				_dbInstance.__init__(self, table, **fields)
		return newClass

class _dbInstance(object):
	def __init__(self, table=None, **fields):
		self._table = table
		self._fields = fields.copy()
		self._oldFields = fields.copy()
		self._upToDate = False
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
	def delete(self):
		return self._table._objectDelete(self)
	def sync(self):
		if not self._upToDate:
			self._table._objectUpdate(self)
			self._oldFields = self._fields.copy()
			self._upToDate = True
