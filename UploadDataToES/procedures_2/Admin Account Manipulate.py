from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "bool": {
                "should": [
                  {
                    "bool": {
                      "should": [
                        {
                          "bool": {
                            "must": [
                              {
                                "match_phrase": {
                                  "event_id": "4738"
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
                                  "event_id": "5136"
                                }
                              },
                              {
                                "match_phrase": {
                                  "dsobject_attribute_name": "msDS-AllowedToDelegateTo"
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
                      "must": [
                        {
                          "match_phrase": {
                            "event_id": "5136"
                          }
                        },
                        {
                          "match_phrase": {
                            "dsobject_class": "user"
                          }
                        },
                        {
                          "match_phrase": {
                            "dsobject_attribute_name": "servicePrincipalName"
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
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "5136"
                    }
                  },
                  {
                    "match_phrase": {
                      "dsobject_attribute_name": "msDS-AllowedToActOnBehalfOfOtherIdentity"
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
tactic = "Credential Access"
technique = "Account Manipulation "
procedure = "Admin Account Manipulate"
tech_code = "T1098"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 46)

