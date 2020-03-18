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
                    "wildcard": {
                      "process_path.keyword": "*\\\\csc.exe"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*\\\\AppData\\\\*"
                          }
                        },
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*\\\\windows\\\\temp\\\\*"
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
                                  "process_parent_path.keyword": "C:\\\\Program Files*"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_parent_path.keyword": "*\\\\sdiagnhost.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_parent_path.keyword": "*\\\\w3wp.exe"
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
tactic = "Defense Evasion"
technique = "Compile After Delivery"
procedure = "Compile After Delivery using csc.exe"
tech_code = "T1500"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 57)

