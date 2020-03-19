from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "process_path": "*\\\\pcalua.exe"
          }
        },
        {
          "wildcard": {
            "process_command_line.keyword": "*-a*"
          }
        }
      ]
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Defense Evasion"
technique = "Indirect Command Execution"
procedure = "Indirect Command Execution - pcalua.exe"
tech_code = "T1202"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 81)

