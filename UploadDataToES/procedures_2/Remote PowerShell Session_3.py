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
                      "event_id": "4103"
                    }
                  },
                  {
                    "match_phrase": {
                      "event_id": "400"
                    }
                  }
                ]
              }
            },
            {
              "match": {
                "powershell.host.name": "ServerRemoteHost"
              }
            },
            {
              "match": {
                "powershell.host.application": "wsmprovhost.exe"
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
tactic = "Execution"
technique = "PowerShell"
procedure = "Remote PowerShell Session"
tech_code = "T1086"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 28)

