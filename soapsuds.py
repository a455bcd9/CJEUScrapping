from suds.client import Client
from suds.wsse import *
import logging
import logging.handlers

client = Client('http://eur-lex.europa.eu/eurlex-ws?wsdl')
# print client

security = Security()
token = UsernameToken('username', 'password')
security.tokens.append(token)
client.set_options(wsse=security)

logging.getLogger('suds.client').setLevel(logging.CRITICAL)
result = client.service.doQuery(expertQuery="DTS_SUBDOM = EU_CASE_LAW", page=1, pageSize=1, searchLanguage="fr")

print recursive_translation(result)