__author__ = 'michelantunes'
import ldap
from pyldap.ldapmodel import LdapAttrib #LdapConfiguration, LdapUser
from pyldap.ldapexception import LdapUserNotFind, LdapSearchException
'''
    Classe responsavel por encapsular as funcoes de comunicacao com LDAP
'''
class LdapManager:
    '''
        Classe responsavel por encapsular as funcoes de comunicacao com LDAP
    '''
    def __init__(self):
        pass

    def getLdapConnection(self, ldapConfig):
        try:
            l = ldap.initialize(ldapConfig.getUrl())
            l.protocol_version = ldapConfig.getLdapVersion()
            return l
        except ldap.LDAPError, e:
            raise

    def closeLdapConnection(self, ldapConn):
        ldapConn.unbind_s()