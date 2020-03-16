from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =  {
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
                            "process_path.keyword": "*\\\\svchost.exe"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\tsmsisrv.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\tsvipsrv.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wlbsctrl.dll"
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
                          "match_phrase": {
                            "event_id": "7"
                          }
                        },
                        {
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\svchost.exe"
                                }
                              }
                            ]
                          }
                        },
                        {
                          "bool": {
                            "should": [
                              {
                                "match_phrase": {
                                  "module_loaded": "C:\\Windows\\WinSxS\\*"
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
tatic = "Defense Evasion"
technique = "DLL Search Order Hijacking"
rule_name = "Svchost DLL Search Order Hijack"
tech_code = "T1038"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

