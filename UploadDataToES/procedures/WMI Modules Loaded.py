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
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "7"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wmiclnt.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\WmiApRpl.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wmiprov.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wmiutils.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wbemcomn.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wbemprox.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\WMINet_Utils.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wbemsvc.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\fastprox.dll"
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must_not": [
                  {
                    "bool": {
                      "must": [
                        {
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\WmiPrvSe.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\WmiAPsrv.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\svchost.exe"
                                }
                              }
                            ]
                          }
                        }
                      ]
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
tactic = "Execution"
technique = "Windows Management Instrumentation"
procedure = "WMI Modules Loaded"
tech_code = "T1047"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 43)

