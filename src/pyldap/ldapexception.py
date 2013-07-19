__author__ = 'michelantunes'

class LdapUserNotFind(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class LdapSearchException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)