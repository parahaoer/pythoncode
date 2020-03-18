from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "bool": {
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "13"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "HKU\\\\*\\\\mscfile\\\\shell\\\\open\\\\command\\\\*"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must": [
                  {
                    "bool": {
                      "must": [
                        {
                          "match_phrase": {
                            "event_id": "1"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\eventvwr.exe"
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
                                  "process_path.keyword": "*\\\\mmc.exe"
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
          ]
        }
      }
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Privilege Escalation"
technique = "Bypass User Account Control"
procedure = "Bypass UAC using Event Viewer"
tech_code = "T1088"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 52)

