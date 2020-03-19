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
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "process_path.keyword": """*\\notepad.exe"""
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": """*\\svchost.exe"""
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": """*\\lsass.exe"""
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": """*\\lsm.exe"""
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": """*\\taskhostw.exe"""
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
                                        "process_parent_path.keyword": """*\\explorer.exe"""
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_parent_path.keyword": """*\\services.exe"""
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_parent_path.keyword": """*\\MsMpEng.exe"""
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_parent_path.keyword": """*\\Mrt.exe"""
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_parent_path.keyword": """*\\rpcnet.exe"""
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_parent_path.keyword": """*\\svchost.exe"""
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
            },
            {
              "bool": {
                "must_not": [
                  {
                    "bool": {
                      "must": [
                        {
                          "bool": {
                            "must_not": {
                              "exists": {
                                "field": "process_parent_path"
                              }
                            }
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
                "must": [
                  {
                    "exists": {
                      "field": "process_command_line"
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
tactic = "Defense Evasion"
technique = "Masquerading"
procedure = "Masquerading"
tech_code = "T1036"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 85)

