__author__ = 'michelantunes'
import ldap

class LdapConfiguration:
    def __init__(self, url, baseDN, ldapVersion=None):
        self.url = url
        self.baseDN = baseDN
        if ldapVersion == 3:
            self.ldapVersion = ldap.VERSION3
        elif ldapVersion is None:
            self.ldapVersion = ldap.VERSION3

    ## GET METHODS
    def getUrl(self):
        return self.url
    def getBaseDN(self):
        return self.baseDN
    def getLdapVersion(self):
        return self.ldapVersion

    ## SET METHODS
    def setUrl(self, url):
        self.url = url
    def setBaseDN(self, baseDN):
        self.baseDN = baseDN
    def setLdapVersion(self, ldapVersion):
        self.ldapVersion = ldapVersion

class LdapUser:
    def __init__(self, user, secret):
        self.user = user
        self.secret = secret

    ## GET METHODS
    def getUser(self):
        return self.user
    def getSecret(self):
        return self.secret
    def getUid(self):
        return self.uid

    ## SET METHODS
    def setUid(self, uid):
        self.uid = uid

class LdapAttrib:
    USER = "uid"
    MAIL = "mail"
    NOME = "cn"