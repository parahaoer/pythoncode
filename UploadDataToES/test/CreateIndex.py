from elasticsearch import Elasticsearch
es = Elasticsearch('helk-elasticsearch:9200')

mappings = {
            "mappings": {
                    "properties": {
                        "id": {
                            "type": "long",

                        },
                        "serial": {
                            "type": "keyword",  # keyword不会进行分词,text会分词

                        },
                        #tags可以存json格式，访问tags.content
                        "tags": {
                            "type": "object",
                            "properties": {
                                "content": {"type": "keyword"},
                                "dominant_color_name": {"type": "keyword"},
                                "skill": {"type": "keyword"},
                            }
                        }
                    }
                }
            }

res = es.indices.create(index = 'index_test',body =mappings)
