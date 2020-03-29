from elasticsearch import Elasticsearch
import datetime
from functools import cmp_to_key

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "size": "10000",
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "11"
          }
        },
        {
          "match": {
            "process_name": "powershell.exe"
          }
        },
        {
          "wildcard": {
            "file_name.keyword": "*\\__psscriptpolicytest_*.ps1"
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

list = res["hits"]["hits"]


def cmp_datetime(a, b):
    a_datetime = getTimeStamp(a)
    b_datetime = getTimeStamp(b)

    if a_datetime.__gt__(b_datetime):
        return 1
    elif a_datetime.__lt__(b_datetime):
        return -1
    else:
        return 0

def getTimeStamp(jsonobj):
  return datetime.datetime.strptime(jsonobj['_source']['@timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')

# list.sort(key = lambda x:getTimeStamp(x))
list.sort(key=cmp_to_key(cmp_datetime))
for doc in list:
    print(doc['_source']['@timestamp'])



