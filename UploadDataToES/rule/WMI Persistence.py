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
tatic = "Execution"
technique = "Windows Management Instrumentation"
rule_name = "WMI Persistence"
tech_code = "T1047"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

