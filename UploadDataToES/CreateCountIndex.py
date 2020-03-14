from elasticsearch import Elasticsearch
es = Elasticsearch('helk-elasticsearch:9200')

mappings = {
            "mappings": {
                    "properties": {
                        "Count": {
                            "type": "long",
                        },
                        "Tatic": {
                            "type": "keyword"
                        },
                        "Technique": {
                            "type": "keyword"
                        },
                        "Rule": {
                            "type": "keyword"
                        },
                        "Tech_code": {
                            "type": "keyword"
                        }
                    }
                }
            }

res = es.indices.create(index = 'represent_5',body =mappings)
