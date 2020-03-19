from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "bool": {
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "4662"
                    }
                  },
                  {
                    "match_phrase": {
                      "object_access_mask_requested": "0x100"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "object_properties.keyword": "*1131f6aa-9c07-11d1-f79f-00c04fc2dcd2*"
                          }
                        },
                        {
                          "wildcard": {
                            "object_properties.keyword": "*1131f6ad-9c07-11d1-f79f-00c04fc2dcd2*"
                          }
                        },
                        {
                          "wildcard": {
                            "object_properties.keyword": "*89e95b76-444d-4c62-991a-0facbeda640c*"
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must_not": [
                  {
                    "bool": {
                      "must": [
                        {
                          "wildcard": {
                            "SubjectUserName|endswith.keyword": "*$"
                          }
                        }
                      ]
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
procedure = "Active Directory Replication from Non Machine Account"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 0)

