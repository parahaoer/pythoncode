from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "param3.keyword": "*DumpCreds*"
                    }
                  },
                  {
                    "wildcard": {
                      "param3.keyword": "*invoke-mimikatz*"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must": [
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "param3.keyword": "*rpc*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*token*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*crypto*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*dpapi*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*sekurlsa*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*kerberos*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*lsadump*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*privilege*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*process*"
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
                            "param3.keyword": "*::*"
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
tatic = "Credential Access"
technique = "Credential Dumping"
rule_name = "Mimikatz Command Line"
tech_code = "T1003"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

