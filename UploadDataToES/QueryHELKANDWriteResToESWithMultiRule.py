from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "20"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "wmi_consumer_destination.keyword": "* -Nop *"
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
tatic = "Execution"
technique = "PowerShell"
rule_name = "Suspicious Scripting in a WMI Consumer"

action ={
            "tatic": tatic,
            "technique": technique,
            "rule_name": rule_name,
            "count": count,
        }

es.index(index="index_test_represent",body = action)

## #rule 2###################################
doc = {
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

action ={
            "tatic": tatic,
            "technique": technique,
            "rule_name": rule_name,
            "count": count,
        }

es.index(index="represent_1",body = action)
