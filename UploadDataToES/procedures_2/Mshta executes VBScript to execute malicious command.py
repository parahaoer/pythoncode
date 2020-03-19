from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "wildcard": {
                "process_parent_path.keyword": "*\\\\mshta.exe"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\cmd.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\powershell.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\wscript.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\cscript.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\sh.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\bash.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\reg.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\regsvr32.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\BITSADMIN*"
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
technique = "Mshta"
procedure = "Mshta executes VBScript to execute malicious command"
tech_code = "T1170"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 94)

