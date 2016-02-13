from pysimplesoap.client import SoapClient
import base64

wsdl = "http://eur-lex.europa.eu/eurlex-ws?wsdl"
# wsdl = "http://158.167.240.227:1043/eurlex-frontoffice/EURLexWebService"
username = 'username'
password = 'password'

xml = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:sear="http://eur-lex.europa.eu/search">
  <soap:Header>
    <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" soap:mustUnderstand="true">
      <wsse:UsernameToken xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="UsernameToken-1">
        <wsse:Username>username</wsse:Username>
        <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">password</wsse:Password>
      </wsse:UsernameToken>
    </wsse:Security>
  </soap:Header>
  <!-- http://eur-lex.europa.eu/eurlex-ws?wsdl -->
  <soap:Body>
    <sear:searchRequest>
      <sear:expertQuery>DTS_SUBDOM = EU_CASE_LAW</sear:expertQuery>
      <sear:page>1</sear:page>
      <!-- Max 100 -->
      <sear:pageSize>1</sear:pageSize>
      <sear:searchLanguage>fr</sear:searchLanguage>
    </sear:searchRequest>
  </soap:Body>
</soap:Envelope>"""

# https://stackoverflow.com/questions/14835542/problems-to-authenticate-correctly-with-pysimplesoap
encoded = base64.b64encode(password)

# https://github.com/pysimplesoap/pysimplesoap/blob/master/pysimplesoap/client.py
# soap12env="http://www.w3.org/2003/05/soap-envelope",
soap_ver = 'soap12env'
client = SoapClient(wsdl=wsdl, trace=True, http_headers={'Authorization': 'Basic %s' % encoded}, soap_ns = soap_ver)

client['wsse:Security'] = {
    'wsse:UsernameToken': {
        'wsse:Username': username,
        'wsse:Password': password,
    }
}    

# expertQuery = 
# response = client.doQuery(xml)

# client.doQuery(searchRequest={'expertQuery': 'DTS_SUBDOM = EU_CASE_LAW', 'page': 1, 'pageSize': 100, 'searchLanguage': 'fr'})

# Help : https://stackoverflow.com/questions/29846470/how-to-construct-soap-message-with-pysimplesoap
client.doQuery(expertQuery = 'DTS_SUBDOM = EU_CASE_LAW', page = 1, pageSize = 100, searchLanguage = 'fr')

# print response

# myProduct = client.getProductByName("ICS_VG")

# https://stackoverflow.com/questions/19021992/how-to-extract-soap-response-using-pysimplesoap
# SimpleXMLElement methods :
# children() to grab childrens list

# repr(response)