from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "bool": {
      "should": [
        {
          "bool": {
            "must": [
              {
                "match": {
                  "process_name": "mshta.exe"
                }
              },
              {
                "wildcard": {
                  "process_command_line.keyword": "*javascript*"
                }
              }
            ]
          }
        },
        {
          "bool": {
            "must": [
              {
                "match": {
                  "process_name": "mshta.exe"
                }
              },
              {
                "match": {
                  "event_id": "3"
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
technique = "Mshta"
procedure = "Mshta executes JavaScript Scheme Fetch Remote Payload With GetObject"
tech_code = "T1170"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

