#!/usr/bin/python
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON
import json

sparql = SPARQLWrapper("http://publications.europa.eu/webapi/rdf/sparql")
sparql.setQuery("""
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
prefix cdm: <http://publications.europa.eu/ontology/cdm#>
select distinct ?celex ?title ?date ?alternative_title ?langue_procedure ?defendeurs ?avocat_gl ?president ?solutions ?national
where {?work a cdm:case-law.
?work cdm:work_date_document ?date.
?word cdm:case-law_national-judgement ?national.
?work cdm:case-case-law_defended_by_agent* ?defendeurs.
?work cdm:case-law_delivered_by_advocate-general* ?avocat_gl.
?work cdm:case-law_delivered_by_judge* ?president.
?work cdm:case-law_has_type_procedure_concept_type_procedure* ?solutions.
?work cdm:resource_legal_id_celex "62014TJ0164"^^xsd:string.
?work cdm:resource_legal_uses_originally_language ?langue_procedure.
?exp cdm:expression_belongs_to_work ?work.
?exp cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/FRA>.
?exp cdm:expression_title ?title.
?exp cdm:expression_title_alternative ?alternative_title.
}
order by desc(?date)
limit 1
""")

# ?work cdm:work_date_document "2016-05-26"^^xsd:date.
# ?work cdm:resource_legal_id_celex "62015CC0230"^^xsd:string.

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# print results["results"]["bindings"]
print json.dumps(results["results"]["bindings"], sort_keys=True,
                indent=4, separators=(',', ': '))

# COURT_NATIONAL_NAME
# 62015CC0047
# 62014TJ0164
# 62015CC0114

# for result in results["results"]["bindings"]:
    # print result["celex"]["value"], result["date"]["value"], result["title"]["value"], result["alternative_title"]["value"]
    # print result["title"]["value"]
