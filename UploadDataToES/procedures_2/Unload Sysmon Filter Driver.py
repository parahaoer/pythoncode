from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "255"
          }
        }
      ]
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Defense Evasion"
technique = "Disabling Security Tools"
procedure = "Unload Sysmon Filter Driver"
tech_code = "T1089"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 111)

