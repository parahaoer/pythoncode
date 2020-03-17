from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "process_name": "regsvr32.exe"
          }
        },
        {
          "bool": {
            "should": [
              {
                "wildcard": {
                  "process_command_line.keyword": "*scrobj*"
                }
              },
              {
                "wildcard": {
                  "process_command_line.keyword": "*/i:*"
                }
              },
              {
                "wildcard": {
                  "process_command_line.keyword": "*-i:*"
                }
              },
              {
                "wildcard": {
                  "process_command_line.keyword": "*.sct*"
                }
              }
            ]
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tatic = "Execution"
technique = "Regsvr32"
procedure = "Regsvr32 remote COM scriptlet Execution"
tech_code = "T1117"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

