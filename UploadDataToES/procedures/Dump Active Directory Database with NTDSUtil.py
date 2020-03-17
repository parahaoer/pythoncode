from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "wildcard": {
          "process_command_line.keyword": "*ntdsutil*"
        }
      }
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tatic = "Credential Access"
technique = "Credential Dumping"
procedure = "Dump Active Directory Database with NTDSUtil"
tech_code = "T1003"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

