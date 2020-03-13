from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
    "query": {
        "match_all": {}
    }
        }


res = es.search(index="index_test",body=doc)

print(res)
