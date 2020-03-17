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
tatic = "Persistence"
technique = "Logon Scripts"
procedure = "Logon Scripts"
tech_code = "T1037"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

