from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc ={
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
tactic = "Execution"
technique = "Trusted Developer Utilities"
procedure = "MSBuild Bypass Using Inline Tasks"
tech_code = "T1127"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 92)

