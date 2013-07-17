__author__ = 'michelantunes'
import ldap
from ldapauth.ldapmodel import LdapAttrib #LdapConfiguration, LdapUser

class LdapManager:
    '''
        Classe responsavel por encapsular as funcoes de comunicacao com LDAP
    '''
    def __init__(self):
        pass

    def search(self, ldapConfig, searchScope,
               searchFilter, retrieveAttributes=None):
        ## TODO Ajustar o metodo para ser generico
        ## first you must open a connection to the server
        try:
	        ## l = ldap.initialize('ldap://mmldap:389')
            l = ldap.initialize(ldapConfig.getUrl())

            ## searching doesn't require a bind in LDAP V3.  If you're using LDAP v2, set the next line appropriately
	        ## and do a bind as shown in the above example.
	        ## you can also set this to ldap.VERSION2 if you're using a v2 directory
	        ## you should  set the next option to ldap.VERSION2 if you're using a v2 directory

            ## l.protocol_version = ldap.VERSION3
            l.protocol_version = ldapConfig.getLdapVersion()

        except ldap.LDAPError, e:
	        print e
	        ## handle error however you like

        ## The next lines will also need to be changed to support your search requirements and directory
        ## baseDN = "dc=gov, dc=br"

        ## retrieve all attributes - again adjust to your needs - see documentation for more options
        ## retrieveAttributes

        ## TODO refletir caracteristicas genericas na busca
        try:
            ldap_result_id = l.search(ldapConfig.getBaseDN(), searchScope, searchFilter, retrieveAttributes)
            result_set = []
            while 1:
                result_type, result_data = l.result(ldap_result_id, 0)
                if (result_data == []):
                    break
                else:
                    ## here you don't have to append to a list
                    ## you could do whatever you want with the individual entry
                    ## The appending to list is just for illustration.
                    if result_type == ldap.RES_SEARCH_ENTRY:
                        result_set.append(result_data)
                        #print result_data[0][0]

            #print result_set
            return result_set
        except ldap.LDAPError, e:
            print e
        finally:
            l.unbind_s()

    def search_auth_user(self, ldapConfig, ldapUser):
        print "search_auth_user - init"
        searchScope = ldap.SCOPE_SUBTREE
        searchFilter = LdapAttrib.USER+"="+ ldapUser.getUser()
        result_arr = []
        result_arr = self.search(ldapConfig, searchScope, searchFilter)

        ## TODO mudar exception
        if (result_arr == []):
            return RuntimeError
        elif (result_arr.__len__() == 1):
            print "Length = 1"
            print result_arr[0][0][0]
            return result_arr[0][0][0]
        else:
            return RuntimeError

    def login(self, ldapConfig, ldapUser):
        try:
            l = ldap.initialize(ldapConfig.getUrl())
        except ldap.LDAPError, e:
            ## TODO tratar melhor
	        print e

        try:
            test = l.simple_bind_s(ldapUser.getUid(), ldapUser.getSecret())
            print test
            ldap_who = l.whoami_s()
            print ldap_who
        except ldap.INVALID_CREDENTIALS, inv_cred:
            print inv_cred
        finally:
            l.unbind_s()