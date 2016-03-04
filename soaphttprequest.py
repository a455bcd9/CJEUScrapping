import requests
url="http://eur-lex.europa.eu/EURLexWebService"
headers = {'content-type': 'application/soap+xml; charset=utf-8'}
# Soap 1.2

body = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:sear="http://eur-lex.europa.eu/search">
<soap:Header>
<wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" soap:mustUnderstand="true">
<wsse:UsernameToken xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="UsernameToken-1">
<wsse:Username></wsse:Username>
<wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText"></wsse:Password>
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

response = requests.post(url,data=body,headers=headers)
# print response.json()
print response.content
# print response.encoding