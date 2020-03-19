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
                "event_id": "13"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\services\\\\TermService\\\\Parameters\\\\ServiceDll*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\Control\\\\Terminal Server\\\\fSingleSessionPerUser*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\Control\\\\Terminal Server\\\\fDenyTSConnections*"
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
tactic = "Defense Evasion"
technique = "Modify Registry"
procedure = "RDP Sensitive Settings Changed"
tech_code = "T1112"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 25)

