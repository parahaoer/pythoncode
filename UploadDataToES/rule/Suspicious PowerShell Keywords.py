from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "match_phrase": {
                "param3": "System.Reflection.Assembly.Load"
              }
            },
            {
              "match_phrase": {
                "param3": "[System.Reflection.Assembly]::Load"
              }
            },
            {
              "match_phrase": {
                "param3": "[Reflection.Assembly]::Load"
              }
            },
            {
              "match_phrase": {
                "param3": "System.Reflection.AssemblyName"
              }
            },
            {
              "match_phrase": {
                "param3": "Reflection.Emit.AssemblyBuilderAccess"
              }
            },
            {
              "match_phrase": {
                "param3": "Runtime.InteropServices.DllImportAttribute"
              }
            },
            {
              "match_phrase": {
                "param3": "SuspendThread"
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
tatic = "Execution"
technique = "PowerShell"
rule_name = "Suspicious PowerShell Keywords"
tech_code = "T1086"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": "T1086",
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

