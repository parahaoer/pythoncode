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
                  "should": [
                    {
                      "match_phrase": {
                        "event_id": "11"
                      }
                    },
                    {
                      "match_phrase": {
                        "event_id": "12"
                      }
                    },
                    {
                      "match_phrase": {
                        "event_id": "13"
                      }
                    },
                    {
                      "match_phrase": {
                        "event_id": "14"
                      }
                    }
                  ]
                }
              },
              {
                "wildcard": {
                  "registry_key_path.keyword": "*UserInitMprLogonScript*"
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
tactic = "Persistence"
technique = "Logon Scripts"
procedure = "Logon Scripts"
tech_code = "T1037"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 84)

