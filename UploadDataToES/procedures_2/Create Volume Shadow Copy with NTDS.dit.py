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
                "process_command_line": "vssadmin.exe Delete Shadows"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "vssadmin.exe create shadow /for=C:"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "copy \\\\\\\\?\\\\GLOBALROOT\\\\Device\\\\*\\\\windows\\\\ntds\\\\ntds.dit"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "copy \\\\\\\\?\\\\GLOBALROOT\\\\Device\\\\*\\\\config\\\\SAM"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "vssadmin delete shadows /for=C:"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "reg SAVE HKLM\\SYSTEM "
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "esentutl.exe /y /vss *\\\\ntds.dit*"
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
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Create Volume Shadow Copy with NTDS.dit"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 63)

