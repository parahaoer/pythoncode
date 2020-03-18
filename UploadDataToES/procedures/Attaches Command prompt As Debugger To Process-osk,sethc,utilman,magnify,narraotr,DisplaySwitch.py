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
                "process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\sethc.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\utilman.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\osk.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\magnify.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\CurrentVersion\\\\Image File Execution Options\\\\narrator.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\displayswitch.exe*"
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
technique = "Accessibility Features"
procedure = "Attaches Command prompt As Debugger To Process-osk,sethc,utilman,magnify,narraotr,DisplaySwitch"
tech_code = "T1015"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 48)

