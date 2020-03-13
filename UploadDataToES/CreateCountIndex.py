from elasticsearch import Elasticsearch
es = Elasticsearch('helk-elasticsearch:9200')

mappings = {
            "mappings": {
                    "properties": {
                        "count": {
                            "type": "long",
                        },
                        "tatic": {
                            "type": "keyword"
                        },
                        "technique": {
                            "type": "keyword"
                        },
                        "rule_name": {
                            "type": "keyword"
                        }
                    }
                }
            }

res = es.indices.create(index = 'index_test_represent',body =mappings)
