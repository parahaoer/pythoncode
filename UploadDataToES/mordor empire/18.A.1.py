from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

search_doc_a = {
  "size": 10000,
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "800"
              }
            },
            {
              "match_phrase": {
                "param3": "name=\"Command\"; value=\"Get-Childitem -Path FileSystem::\\\\HFDC01\\IT\\\""
              }
            }
          ]
        }
      }
    }
  }
}

res_a = es.search(index="logs-endpoint-winevent-*",body=search_doc_a)

count = res_a['hits']['total']['value']

tactic = "Discovery"
technique = "File and Directory Discovery"
tech_code = "T1083"
eval_phase = "Collection"
eval_step = "18.A.1"

action = {
  "Tactic": tactic,
  "Technique": technique,
  "Tech_code": tech_code,
  "EvalStep": eval_step,
  "EvalPhase": eval_phase,
  "EventCount": count,
}

es.index(index="represent_7", body=action, id=28)
