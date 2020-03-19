from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =   {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "5136"
              }
            },
            {
              "match_phrase": {
                "dsobject_attribute_name": "ntSecurityDescriptor"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "match": {
                      "dsobject_attribute_value": "1131f6ad-9c07-11d1-f79f-00c04fc2dcd2"
                    }
                  },
                  {
                    "match": {
                      "dsobject_attribute_value": "*1131f6aa-9c07-11d1-f79f-00c04fc2dcd2*"
                    }
                  },
                  {
                    "match": {
                      "dsobject_attribute_value": "*89e95b76-444d-4c62-991a-0facbeda640c*"
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    }
  }
}



res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Powerview Add-DomainObjectAcl DCSync AD Extend Right"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 23)

