__author__ = 'michelantunes'
from ldapauth.ldapmanager import LdapManager
from ldapauth.ldapmodel import LdapConfiguration, LdapUser

ldapConfig = LdapConfiguration("ldap://ldap:389","dc=corp, dc=br")

#user = raw_input("Informe usuario:")
user = "name"
#secret = raw_input("Informe senha:")
secret = ""

ldapUser = LdapUser(user, secret)

result_uid = LdapManager().search_auth_user(ldapConfig,ldapUser)

ldapUser.setUid(result_uid)

LdapManager().login(ldapConfig, ldapUser)
