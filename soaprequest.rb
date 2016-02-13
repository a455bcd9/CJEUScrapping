require 'savon'
require 'builder'

client = Savon.client do
  wsdl 'http://eur-lex.europa.eu/eurlex-ws?wsdl'
  wsse_auth 'username', 'password'
  soap_version 2
end

p client.operations
p client.call(:do_query, message: {
                'sear:expertQuery' => 'DTS=6',
                'sear:page' => 1,
                'sear:pageSize' => 10,
                'sear:searchLanguage' => 'en'
                })