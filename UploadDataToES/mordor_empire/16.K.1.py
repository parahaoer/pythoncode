from functools import cmp_to_key
from elasticsearch import Elasticsearch
import datetime


es = Elasticsearch('helk-elasticsearch:9200')

search_doc_a = {
  "size": 10000,
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "800"
              }
            },
            {
              "match_phrase": {
                "param3": "name=\"Command\"; value=\"type FileSystem::\"\\\\HFDC01\\C$\\Users\\pgustavo\\AppData\\Roaming\\Adobe\\Flash Player\\autoupdate.vbs\"\""
              }
            }
          ]
        }
      }
    }
  }
}

search_doc_b = {
  "size": 10000,
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "4103"
          }
        },
        {
          "match_phrase": {
            "powershell.param.value": "type FileSystem::\"\\\\HFDC01\\C$\\Users\\pgustavo\\AppData\\Roaming\\Adobe\\Flash Player\\autoupdate.vbs\""
          }
        }
      ]
    }
  }
}

def getTimeStamp(jsonobj):
  return datetime.datetime.strptime(jsonobj['_source']['@timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')

def getTimeDifference(jsonobjA, jsonobjB):
  timeA = getTimeStamp(jsonobjA)
  timeB = getTimeStamp(jsonobjB)
  if timeA.__gt__(timeB):
    return (timeA - timeB).seconds
  else:
    return (timeB-timeA).seconds

#定义时间比较器，用于排序
def cmp_datetime(a, b):
  a_datetime = getTimeStamp(a)
  b_datetime = getTimeStamp(b)

  if a_datetime.__gt__(b_datetime):
    return 1
  elif a_datetime.__lt__(b_datetime):
    return -1
  else:
    return 0


res_a = es.search(index="logs-endpoint-winevent-*",body=search_doc_a)
res_b = es.search(index="logs-endpoint-winevent-*",body=search_doc_b)


list_a =res_a["hits"]["hits"]
list_b =res_b["hits"]["hits"]


# 对list_a、list_b、list_c 列表分别按照时间先后排序
list_a.sort(key=cmp_to_key(cmp_datetime))
list_b.sort(key=cmp_to_key(cmp_datetime))

count = 0

for a_doc in list_a:
  for b_doc in list_b:
    if(getTimeDifference(a_doc, b_doc) <= 1):
      count = count + 1
      list_a.remove(a_doc)
      list_b.remove(b_doc)

print(count)

tactic = "Discovery"
technique = "File and Directory Discovery"
tech_code = "T1083"
eval_phase = "Lateral Movement"
eval_step = "16.K.1"

action = {
  "Tactic": tactic,
  "Technique": technique,
  "Tech_code": tech_code,
  "EvalStep": eval_step,
  "EvalPhase": eval_phase,
  "EventCount": count,
}

es.index(index="represent_7", body=action, id=23)
