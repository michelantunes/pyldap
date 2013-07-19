__author__ = 'michelantunes'
from pyldap.control.ldapmanager import LdapManager
from pyldap.ldapmodel import LdapConfiguration, LdapUser
import getpass, sys

ldapConfig = LdapConfiguration("ldap://ldap:389","dc=corp, dc=br")

#user = raw_input("Informe usuario:")
user = "michelantunes"
#secret = raw_input("Informe senha:")

if sys.stdin.isatty():
    secret = getpass.getpass('Informe a senha: ')
else:
    print 'Informe a senha:'
    secret = sys.stdin.readline().rstrip()

#secret = ""

ldapUser = LdapUser(user, secret)

LdapManager().login(ldapConfig, ldapUser)
