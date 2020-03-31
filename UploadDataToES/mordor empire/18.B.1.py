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
                "param1": "Copy-Item FileSystem::\\\\HFDC01\\IT\\recipe.txt C:\\\"$\"Recycle.Bin\\recipe.txt"
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

tactic = "Collection"
technique = "Data Staged"
tech_code = "T1074"
eval_phase = "Collection"
eval_step = "18.B.1"

action = {
  "Tactic": tactic,
  "Technique": technique,
  "Tech_code": tech_code,
  "EvalStep": eval_step,
  "EvalPhase": eval_phase,
  "EventCount": count,
}

es.index(index="represent_7", body=action, id=29)
