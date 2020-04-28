from functools import cmp_to_key
# pycharm 默认该项目的根目录为sources Root，所以引用不到。
#from procedures.threeRule_info import
# 用相对路径引入， .表示当前路径
from .shell_threeRule_info import rule_1_list, rule_2_list, rule_3_list,tactic_list, technique_list, technique_id_list, eval_phase_list, eval_step_list
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
              "powershell.param.value": ""
            }
          }
        ]
      }
    }
  }

  search_doc_b["query"]["bool"]["must"][1]["match_phrase"]["powershell.param.value"] = rule_2_list[id]

  search_doc_c = {
    "size": 10000,
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "event_id": "4688"
            }
          },
          {
            "match_phrase": {
              "process_command_line": ""
            }
          }
        ]
      }
    }
  }

  search_doc_c["query"]["bool"]["must"][1]["match_phrase"]["process_command_line"] = rule_3_list[id]

  # 使用json.dump将json对象转换成字符串，然后再打印json字符串。否则打印出的内容都是单引号的。
  # if(id == 21):
  #   print(json.dumps(search_doc_a, indent=2))
  #   print(json.dumps(search_doc_b, indent=2))
  #   print(json.dumps(search_doc_c, indent=2))

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
            if(b_doc['_source']['user']['identifier'] == c_doc['_source']['user_sid']):

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

  es.index(index="represent_7",body = action, id = id)










'''
    约束条件：
    1、三条规则返回记录的时间戳在1s内；
    2、第二步规则返回记录中的user.identifier = 第三步规则返回记录中的event_data.SubjectUserSid
    输入：
    三条规则 分别查询得到的记录列表，例如 a=[a_doc_1, a_doc_2]， b=[b_doc_1,b_doc_2], c=[c_doc_1,c_doc_2]
    输出：
    满足约束条件的记录条数
    伪代码：
        1、对记录列表 a、b、c分别按照时间先后排序。
        2、满足约束条件的记录条数 count = 0
        3、
        for a_doc in a：
            for b_doc in b：
                if(|a_doc.timestamp - b_doc.timestamp| < 1s):
                    for c_doc in c:
                        if(|a_doc.timestamp - c_doc.timestamp| < 1s and |b_doc.timestamp - c_doc.timestamp| < 1s):
                            if(b_doc.user.identifier == c_doc.event_data.SubjectUserSid):
                                count = count + 1
                                a.remove(a_doc)
                                b.remove(b_doc)
                                c.remove(c_doc)
        return count

'''
def Restrictions():
    pass