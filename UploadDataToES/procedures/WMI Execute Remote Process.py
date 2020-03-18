from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "process_name": "wmic.exe"
          }
        },
        {
          "bool": {
            "should": [
              {
                "wildcard": {
                  "process_command_line.keyword": {
                    "value": "* /node:*"
                  }
                }
              },
              {
                "wildcard": {
                  "process_command_line.keyword": {
                    "value": "* -node:*"
                  }
                }
              }
            ]
          }
        },
        {
          "wildcard": {
            "process_command_line.keyword": {
              "value": "* *process* call *"
            }
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Execution"
technique = "Windows Management Instrumentation"
procedure = "WMI Execute Remote Process"
tech_code = "T1047"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 118)

