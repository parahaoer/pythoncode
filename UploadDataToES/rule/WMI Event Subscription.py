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
                "event_id": "19"
              }
            },
            {
              "match_phrase": {
                "event_id": "20"
              }
            },
            {
              "match_phrase": {
                "event_id": "21"
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
technique = "Windows Management Instrumentation Event Subscription"
rule_name = "WMI Event Subscription"
tech_code = "T1084"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

