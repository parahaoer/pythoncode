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
                                  "user_reporter_sid": "S-1-0-0"
                                }
                              },
                              {
                                "match_phrase": {
                                  "logon_type": "3"
                                }
                              },
                              {
                                "match_phrase": {
                                  "logon_process_name": "ntlmssp"
                                }
                              },
                              {
                                "match_phrase": {
                                  "logon_key_length": "0"
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
tactic = "Lateral Movement"
technique = "Pass the Hash"
procedure = "Pass the Hash Activity 2"
tech_code = "T1175"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 19)

