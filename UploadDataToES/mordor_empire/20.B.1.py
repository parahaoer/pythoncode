from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

search_doc_a = {
  "size": 10000,
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "1"
          }
        },
        {
          "match": {
            "process_name": "whoami.exe"
          }
        },
        {
          "match": {
            "file_description": "whoami - displays logged on user information"
          }
        }
      ]
    }
  }
}

res_a = es.search(index="logs-endpoint-winevent-*",body=search_doc_a)

count = res_a['hits']['total']['value']

tactic = "Discovery"
technique = "System Owner/User Discovery"
tech_code = "T1033"
eval_phase = "Execution of Persistence"
eval_step = "20.B.1"

action = {
  "Tactic": tactic,
  "Technique": technique,
  "Tech_code": tech_code,
  "EvalStep": eval_step,
  "EvalPhase": eval_phase,
  "EventCount": count,
}

es.index(index="represent_7", body=action, id=50)
