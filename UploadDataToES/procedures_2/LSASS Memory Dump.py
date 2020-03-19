from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "10"
              }
            },
            {
              "match_phrase": {
                "process_target_path": """C:\windows\system32\lsass.exe"""
              }
            },
            {
              "match_phrase": {
                "process_granted_access": "2097151"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_call_trace.keyword": "*dbghelp.DLL*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_call_trace.keyword": "*dbgcore.DLL*"
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
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "LSASS Memory Dump"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 10)

