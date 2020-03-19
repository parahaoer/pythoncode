from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =    {
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
              "match_phrase": {
                "event_type": "SetValue"
              }
            },
            {
              "bool": {
                "must": [
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\Control\\\\SecurityProviders\\\\WDigest\\\\UseLogonCredential"
                    }
                  },
                  {
                    "match_phrase": {
                      "registry_key_value": "1"
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
procedure = "Chafer Activity"
tech_code = "T1112"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 3)

