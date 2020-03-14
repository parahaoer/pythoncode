from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "5156"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "match_phrase": {
                      "dst_port": "5985"
                    }
                  },
                  {
                    "match_phrase": {
                      "dst_port": "5986"
                    }
                  }
                ]
              }
            },
            {
              "match_phrase": {
                "network_layer_id": "44"
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
tatic = "Execution"
technique = "PowerShell"
rule_name = "Remote PowerShell Session"
tech_code = "T1086"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

