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
                      "process_path.keyword": "*\\\\attrib.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* +h *"
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
                      "should": [
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*\\\\desktop.ini *"
                          }
                        },
                        {
                          "bool": {
                            "must": [
                              {
                                "wildcard": {
                                  "process_parent_path.keyword": "*\\\\cmd.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_command_line.keyword": "+R +H +S +A \\\\*.cui"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_parent_command_line.keyword": "C:\\\\WINDOWS\\\\system32\\\\*.bat"
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
tactic = "Persistence"
technique = "Hidden Files and Directories"
procedure = "Create Windows System File with Attrib"
tech_code = "T1158"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 65)

