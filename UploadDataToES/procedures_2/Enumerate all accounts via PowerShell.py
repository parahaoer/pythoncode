from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\whoami.exe"
                    }
                  },
                  {
                    "bool": {
                      "must": [
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\wmic.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*useraccount*"
                          }
                        },
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*get*"
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
                            "process_path.keyword": "*\\\\quser.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\qwinsta.exe"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "must": [
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\cmdkey.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*/list*"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "must": [
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\cmd.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*/c*"
                          }
                        },
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*dir*"
                          }
                        },
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*\\\\Users\\\\*"
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
                    "bool": {
                      "must": [
                        {
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\net.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\net1.exe"
                                }
                              }
                            ]
                          }
                        },
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*user*"
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
                                        "process_command_line.keyword": "*/domain*"
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_command_line.keyword": "*/add*"
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_command_line.keyword": "*/delete*"
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_command_line.keyword": "*/active*"
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_command_line.keyword": "*/expires*"
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_command_line.keyword": "*/passwordreq*"
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_command_line.keyword": "*/scriptpath*"
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_command_line.keyword": "*/times*"
                                      }
                                    },
                                    {
                                      "wildcard": {
                                        "process_command_line.keyword": "*/workstations*"
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
          ]
        }
      }
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Discovery"
technique = "Account Discovery"
procedure = "Enumerate all accounts via PowerShell"
tech_code = "T1087"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 73)

