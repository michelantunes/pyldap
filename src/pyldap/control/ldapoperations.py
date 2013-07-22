__author__ = 'michelantunes'
import ldap
from pyldap.control.ldapmanager import LdapManager
from pyldap.ldapmodel import LdapAttrib #LdapConfiguration, LdapUser
from pyldap.ldapexception import LdapUserNotFind, LdapSearchException
'''
    Classe responsavel por encapsular as operacoes com LDAP
'''
class LdapOperations:
    '''
        Method
    '''
    def __init__(self):
        pass

    '''
        Method
    '''
    def search(self, ldapConfig, searchScope,
               searchFilter, retrieveAttributes=None):

        ldapManager = LdapManager()
        ## first you must open a connection to the server
        try:
            #l = ldap.initialize(ldapConfig.getUrl())
            
            ## searching doesn't require a bind in LDAP V3.  If you're using LDAP v2, set the next line appropriately
            ## and do a bind as shown in the above example.
            ## you can also set this to ldap.VERSION2 if you're using a v2 directory
            ## you should  set the next option to ldap.VERSION2 if you're using a v2 directory

            #l.protocol_version = ldapConfig.getLdapVersion()

            l = ldapManager.getLdapConnection(ldapConfig)

        except ldap.LDAPError, e:
            raise

        ## The next lines will also need to be changed to support your search requirements and directory
        ## baseDN = "dc=gov, dc=br"

        ## retrieve all attributes - again adjust to your needs - see documentation for more options

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

            return result_set
        except ldap.LDAPError, e:
            raise
        finally:
            ldapManager.closeLdapConnection(l)
            #l.unbind_s()

    '''
        Method
    '''
    def __search_auth_user(self, ldapConfig, ldapUser):
        
        searchScope = ldap.SCOPE_SUBTREE
        searchFilter = LdapAttrib.USER+"="+ ldapUser.getUser()
        result_arr = []
        result_arr = self.search(ldapConfig, searchScope, searchFilter)

        if (result_arr == []) or (result_arr is None):
            raise LdapUserNotFind("Do not find user: "+ldapUser.getUser())
        elif (result_arr.__len__() == 1):
            return result_arr[0][0][0]
        else:
            raise LdapSearchException("A search error occurred. Result: "+str(result_arr))

    '''
        Method
    '''
    def login(self, ldapConfig, ldapUser):
        #TODO Return something
        # Searching for user id
        ldapOper = LdapOperations()
        result_uid = ldapOper.__search_auth_user(ldapConfig,ldapUser)
        ldapUser.setUid(result_uid)

        ldapManager = LdapManager()

        try:
            #l = ldap.initialize(ldapConfig.getUrl())
            #l.protocol_version = ldapConfig.getLdapVersion()
            l = ldapManager.getLdapConnection(ldapConfig)
        except ldap.LDAPError, e:
            raise

        try:
            test = l.simple_bind_s(ldapUser.getUid(), ldapUser.getSecret())
            #print str(test)
            ldap_who = l.whoami_s()
            print "\nSuccessful Logon!!\n USER: " + str(ldap_who)

        except ldap.INVALID_CREDENTIALS, inv_cred:
            #print inv_cred
            raise
        finally:
            ldapManager.closeLdapConnection(l)
            #l.unbind_s()
