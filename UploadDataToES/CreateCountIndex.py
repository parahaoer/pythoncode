from elasticsearch import Elasticsearch
es = Elasticsearch('helk-elasticsearch:9200')

mappings = {
            "mappings": {
                    "properties": {
                        "EventCount": {
                            "type": "long",
                        },
                        "Tactic": {
                            "type": "keyword"
                        },
                        "Technique": {
                            "type": "keyword"
                        },
                        "Procedure": {
                            "type": "keyword"
                        },
                        "Tech_code": {
                            "type": "keyword"
                        }
                    }
                }
            }

res = es.indices.create(index = 'represent_6',body =mappings)
