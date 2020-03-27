from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "4103"
          }
        },
        {
          "match_phrase": {
            "powershell.param.value": "route print"
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

list_a =res["hits"]["hits"]

for doc_a in list_a:
    print(doc_a['_source']["@timestamp"])


