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
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* group*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* localgroup*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* user*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* view*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* share"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* accounts*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* use*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* stop *"
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
procedure = "Net.exe Execution"
tech_code = "T1087"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 17)

