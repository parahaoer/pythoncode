from functools import cmp_to_key
# pycharm 默认该项目的根目录为sources Root，所以引用不到。
#from procedures.threeRule_info import
# 用相对路径引入， .表示当前路径
from .RuleForUpload_info import rule_1_list, rule_3_list,tactic_list, technique_list, technique_id_list, eval_phase_list, eval_step_list
from elasticsearch import Elasticsearch
import datetime
import json

es = Elasticsearch('helk-elasticsearch:9200')


def getTimeStamp(jsonobj):
  return datetime.datetime.strptime(jsonobj['_source']['@timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')


def getTimeDifference(jsonobjA, jsonobjB):
  timeA = getTimeStamp(jsonobjA)
  timeB = getTimeStamp(jsonobjB)
  if timeA.__gt__(timeB):
    return (timeA - timeB).seconds
  else:
    return (timeB - timeA).seconds


# 定义时间比较器，用于排序
def cmp_datetime(a, b):
  a_datetime = getTimeStamp(a)
  b_datetime = getTimeStamp(b)

  if a_datetime.__gt__(b_datetime):
    return 1
  elif a_datetime.__lt__(b_datetime):
    return -1
  else:
    return 0

for id in range(len(rule_1_list)):
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
                  "param3": ""
                }
              }
            ]
          }
        }
      }
    }
  }

  search_doc_a["query"]["constant_score"]["filter"]["bool"]["must"][1]["match_phrase"]["param3"] = rule_1_list[id]

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
              "powershell.command.name": "Set-Content"
            }
          }
        ]
      }
    }
  }

  search_doc_c = {
    "size": 10000,
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "event_id": "11"
            }
          },
          {
            "match_phrase": {
              "file_name": ""
            }
          }
        ]
      }
    }
  }

  search_doc_c["query"]["bool"]["must"][1]["match_phrase"]["file_name"] = rule_3_list[id]

  res_a = es.search(index="logs-endpoint-winevent-*",body=search_doc_a)
  res_b = es.search(index="logs-endpoint-winevent-*",body=search_doc_b)
  res_c = es.search(index="logs-endpoint-winevent-*",body=search_doc_c)

  list_a =res_a["hits"]["hits"]
  list_b =res_b["hits"]["hits"]
  list_c =res_c["hits"]["hits"]

  # 对list_a、list_b、list_c 列表分别按照时间先后排序
  list_a.sort(key=cmp_to_key(cmp_datetime))
  list_b.sort(key=cmp_to_key(cmp_datetime))
  list_c.sort(key=cmp_to_key(cmp_datetime))

  count = 0

  for a_doc in list_a:
    for b_doc in list_b:
      if(getTimeDifference(a_doc, b_doc) <= 1):
        for c_doc in list_c:

          if(getTimeDifference(a_doc, c_doc) <= 1 and getTimeDifference(b_doc, c_doc) <= 1):

              count = count + 1
              list_a.remove(a_doc)
              list_b.remove(b_doc)
              list_c.remove(c_doc)
  print(count)

  tactic = tactic_list[id]
  technique = technique_list[id]
  tech_code = technique_id_list[id]
  eval_phase = eval_phase_list[id]
  eval_step = eval_step_list[id]

  action ={
              "Tactic": tactic,
              "Technique": technique,
              "Tech_code": tech_code,
              "EvalStep": eval_step,
              "EvalPhase": eval_phase,
              "EventCount": count,
          }

  es.index(index="represent_7",body = action, id = id+44)
