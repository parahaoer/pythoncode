from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_parent_path.keyword": "*\\\\powershell.exe"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*schtasks*/create*/sc *ONLOGON*/TN *Updater*/TR *powershell*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*schtasks*/create*/sc *daily*/tn *updater*/tr *powershell*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*schtasks*/Create*/SC *ONIDLE*/TN *Updater*/TR *powershell*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*schtasks*/Create*/SC *Updater*/TN *Updater*/TR *powershell*"
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
tactic = "Persistence"
technique = "Scheduled Task"
procedure = "Default PowerSploit and Empire Schtasks Persistence"
tech_code = "T1053"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 5)

