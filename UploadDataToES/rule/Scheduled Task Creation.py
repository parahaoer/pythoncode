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
                      "process_path.keyword": "*\\\\schtasks.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* /create *"
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
                            "user_account": "NT AUTHORITY\\SYSTEM"
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
tatic = "Persistence"
technique = "Scheduled Task"
rule_name = "Scheduled Task Creation"
tech_code = "T1053"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

