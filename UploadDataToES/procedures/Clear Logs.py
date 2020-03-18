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
                      "process_path.keyword": "*\\\\wevtutil.exe"
                    }
                  },
                  {
                    "match_phrase": {
                      "file_name_original": "wevtutil.exe"
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
                      "process_command_line.keyword": "* cl *"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* clear-log *"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* sl *"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* set-log *"
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
technique = "Indicator Removal on Host"
procedure = "Clear Logs"
tech_code = "T1070"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 56)

