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
                "event_id": "20"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "wmi_consumer_destination.keyword": "* -Nop *"
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

print(type(res))  ## res 是字典

print(res.keys())

print(res['hits']['total']['value'])
