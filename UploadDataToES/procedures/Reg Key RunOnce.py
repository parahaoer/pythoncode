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
                "event_id": "13"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run\\\\*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunOnce\\\\*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunOnceEx\\\\*"
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

count = res['hits']['total']['value']
tatic = "Persistence"
technique = "Registry Run Keys/Startup Folder"
procedure = "Reg Key RunOnce"
tech_code = "T1060"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

