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
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "System.Reflection.Assembly.Load"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "[System.Reflection.Assembly]::Load"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "[Reflection.Assembly]::Load"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "System.Reflection.AssemblyName"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "Reflection.Emit.AssemblyBuilderAccess"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "Runtime.InteropServices.DllImportAttribute"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "SuspendThread"
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
technique = "PowerShell"
procedure = "Suspicious PowerShell Keywords"
tech_code = "T1086"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 36)

