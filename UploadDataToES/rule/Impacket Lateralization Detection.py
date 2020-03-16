from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "bool": {
            "should": [
              {
                "wildcard": {
                  "process_parent_path.keyword": """*\\explorer.exe"""
                }
              },
              {
                "wildcard": {
                  "process_parent_path.keyword": """*\\services.exe"""
                }
              },
              {
                "wildcard": {
                  "process_parent_path.keyword": """*\\wmiprvse.exe"""
                }
              },
              {
                "wildcard": {
                  "process_parent_path.keyword": """*\\mmc.exe"""
                }
              }
            ]
          }
        },
        {
          "wildcard": {
            "process_command_line.keyword": {
              "value": """*\\cmd.exe* /c*"""
            }
          }
        }
      ]
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tatic = "Lateral Movement"
technique = "Component Object Model and Distributed COM"
rule_name = "Impacket Lateralization Detection"
tech_code = "T1175"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

