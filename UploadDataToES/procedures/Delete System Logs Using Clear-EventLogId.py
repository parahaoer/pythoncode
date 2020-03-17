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
                "event_id": "104"
              }
            },
            {
              "match_phrase": {
                "source_name": "Microsoft-Windows-Eventlog"
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
tatic = "Defense Evasion"
technique = "Indicator Removal on Host"
procedure = "Delete System Logs Using Clear-EventLogId"
tech_code = "T1070"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

