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
                "process_command_line.keyword": "*\\\\rundll32.exe* url.dll,*OpenURL *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\rundll32.exe* url.dll,*OpenURLA *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\rundll32.exe* url.dll,*FileProtocolHandler *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\rundll32.exe* zipfldr.dll,*RouteTheCall *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\rundll32.exe* Shell32.dll,*Control_RunDLL *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\rundll32.exe javascript:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* url.dll,*OpenURL *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* url.dll,*OpenURLA *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* url.dll,*FileProtocolHandler *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* zipfldr.dll,*RouteTheCall *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* Shell32.dll,*Control_RunDLL *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* javascript:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*.RegisterXLL*"
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
technique = "Rundll32"
procedure = "Rundll32 execute JavaScript Remote Payload With GetObject"
tech_code = "T1085"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 109)

