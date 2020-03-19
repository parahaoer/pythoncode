from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "12"
              }
            },
            {
              "match_phrase": {
                "registry_key_path": "HKU\\*"
              }
            },
            {
              "wildcard": {
                "registry_key_path.keyword": "*_Classes\\\\CLSID\\\\*"
              }
            },
            {
              "wildcard": {
                "registry_key_path.keyword": "*\\\\TreatAs"
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
technique = "Component Object Model Hijacking"
procedure = "Component Object Model Hijacking"
tech_code = "T1197"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 58)

