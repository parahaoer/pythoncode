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
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "4624"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "bool": {
                            "must": [
                              {
                                "match_phrase": {
                                  "SubjectUserSid": "S-1-0-0"
                                }
                              },
                              {
                                "match_phrase": {
                                  "logon_type": "3"
                                }
                              },
                              {
                                "match_phrase": {
                                  "logon_process_name": "NtLmSsp"
                                }
                              },
                              {
                                "match_phrase": {
                                  "KeyLength": "0"
                                }
                              }
                            ]
                          }
                        },
                        {
                          "bool": {
                            "must": [
                              {
                                "match_phrase": {
                                  "logon_type": "9"
                                }
                              },
                              {
                                "match_phrase": {
                                  "logon_process_name": "seclogo"
                                }
                              }
                            ]
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must_not": [
                  {
                    "bool": {
                      "must": [
                        {
                          "match_phrase": {
                            "user_name": "ANONYMOUS LOGON"
                          }
                        }
                      ]
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
tatic = "Lateral Movement"
technique = "Pass the Hash"
procedure = "Mimikatz Pass the Hash"
tech_code = "T1075"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

