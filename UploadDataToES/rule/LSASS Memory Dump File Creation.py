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
                "event_id": "11"
              }
            },
            {
              "wildcard": {
                "file_name.keyword": "*lsass*"
              }
            },
            {
              "wildcard": {
                "file_name.keyword": "*dmp"
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
tatic = "Credential Access"
technique = "Credential Dumping"
rule_name = "LSASS Memory Dump File Creation"
tech_code = "T1003"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

