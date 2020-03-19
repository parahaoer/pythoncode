from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "wildcard": {
                "process_command_line.keyword": "* -decode *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /decode *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* -decodehex *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /decodehex *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* -urlcache *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /urlcache *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* -verifyctl *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /verifyctl *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* -encode *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /encode *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*certutil* -URL*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*certutil* /URL*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*certutil* -ping*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*certutil* /ping*"
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
technique = "Deobfuscate/Decode Files or Information"
procedure = "Deobfuscate/Decode Files Or Information"
tech_code = "T1140"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 68)

