from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =   {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "match": {
                "powershell.command.name" : "Invoke-PsExec"
              }
            },
              {
                  "match": {
                     "param3": "*Invoke-DllInjection*"
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
rule_name = "Malicious PowerShell Commandlets"
tech_code = "T1086"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

