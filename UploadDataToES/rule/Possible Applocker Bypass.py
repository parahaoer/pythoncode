from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\msdt.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\installutil.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\regsvcs.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\regasm.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\msbuild.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\ieexec.exe*"
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
technique = ["InstallUtil", "Trusted Developer Utilities"]
rule_name = "Possible Applocker Bypass"
tech_code = ["T1118", "T1127"]

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": "T1086",
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

