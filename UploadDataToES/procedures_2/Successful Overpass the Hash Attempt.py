from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "4624"
              }
            },
            {
              "match_phrase": {
                "logon_type": "9"
              }
            },
            {
              "match_phrase": {
                "logon_process_name": "seclogo"
              }
            },
            {
              "match_phrase": {
                "logon_authentication_package_name": "Negotiate"
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
tactic = "Lateral Movement"
technique = "Pass the Hash"
procedure = "Successful Overpass the Hash Attempt"
tech_code = "T1075"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 34)

