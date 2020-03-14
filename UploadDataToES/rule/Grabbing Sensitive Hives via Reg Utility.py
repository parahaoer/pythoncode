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
                "process_path.keyword": "*\\\\reg.exe"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*save*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*export*"
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
                      "process_command_line.keyword": "*hklm*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*hkey_local_machine*"
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
                      "process_command_line.keyword": "*\\system"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*\\sam"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*\\security"
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
tatic = "Credential Access"
technique = "Credential Dumping"
rule_name = "Grabbing Sensitive Hives via Reg Utility"
tech_code = "T1003"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

