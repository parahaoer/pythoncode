from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "bool": {
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "5861"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "Message.keyword": "*ActiveScriptEventConsumer*"
                          }
                        },
                        {
                          "wildcard": {
                            "Message.keyword": "*CommandLineEventConsumer*"
                          }
                        },
                        {
                          "wildcard": {
                            "Message.keyword": "*CommandLineTemplate*"
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            },
            {
              "match_phrase": {
                "event_id": "5859"
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
technique = "Windows Management Instrumentation"
procedure = "WMI Persistence"
tech_code = "T1047"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 44)

