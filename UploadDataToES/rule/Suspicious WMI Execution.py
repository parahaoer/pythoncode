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
                      "process_path.keyword": "*\\\\wmic.exe"
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
                      "process_command_line.keyword": "*/node:*process call create *"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* path AntiVirusProduct get *"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* path FirewallProduct get *"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* shadowcopy delete *"
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
tatic = "Execution"
technique = "Windows Management Instrumentation"
rule_name = "Suspicious WMI Execution"
tech_code = "T1047"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

