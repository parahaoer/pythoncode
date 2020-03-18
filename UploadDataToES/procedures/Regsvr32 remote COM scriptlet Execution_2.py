from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc ={
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "bool": {
                "must": [
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\regsvr32.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*\\\\Temp\\\\*"
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
                      "process_path.keyword": "*\\\\regsvr32.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_parent_path.keyword": "*\\\\powershell.exe"
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
                      "process_path.keyword": "*\\\\regsvr32.exe"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*/i:http* scrobj.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "process_command_line.keyword": "*/i:ftp* scrobj.dll"
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
                    "wildcard": {
                      "process_path.keyword": "*\\\\wscript.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_parent_path.keyword": "*\\\\regsvr32.exe"
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
                      "process_path.keyword": "*\\\\EXCEL.EXE"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*..\\\\..\\\\..\\\\Windows\\\\System32\\\\regsvr32.exe *"
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
technique = "Regsvr32"
procedure = "Regsvr32 remote COM scriptlet Execution"
tech_code = "T1117"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 108)

