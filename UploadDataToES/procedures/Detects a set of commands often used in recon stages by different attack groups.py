from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "match_phrase": {
                "process_command_line": "tasklist"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "net time"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "systeminfo"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "whoami"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "nbtstat"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "net start"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\net1 start"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "qprocess"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "nslookup"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "hostname.exe"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\net1 user /domain"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\net1 group /domain"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\net1 group \"domain admins\" /domain"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\net1 group \"Exchange Trusted Subsystem\" /domain"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\net1 accounts /domain"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\net1 user net localgroup administrators"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "netstat -an"
              }
            }
          ]
        }
      }
    }
  },
  "size": 0,
  "aggs": {
    "process_command_line_count": {
      "terms": {
        "field": "process_command_line.keyword",
          "order": {
          "_count": "desc"
        },
        "min_doc_count": 4
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

