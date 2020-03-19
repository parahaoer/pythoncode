from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "wildcard": {
                "process_command_line.keyword": "* asreproast *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* dump /service:krbtgt *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* kerberoast *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* createnetonly /program:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* ptt /ticket:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /impersonateuser:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* renew /ticket:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* asktgt /user:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* harvest /interval:*"
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
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Rubeus Hack Tool"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 30)

