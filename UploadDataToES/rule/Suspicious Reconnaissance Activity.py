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
                "param3": "net group \"domain admins\" /domain"
              }
            },
            {
              "match_phrase": {
                "param3": "net localgroup administrators"
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
tatic = "Discovery"
technique = "Account Discovery"
rule_name = "Suspicious Reconnaissance Activity"
tech_code = "T1087"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

