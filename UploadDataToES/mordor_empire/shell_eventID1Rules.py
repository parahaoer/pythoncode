from functools import cmp_to_key
# pycharm 默认该项目的根目录为sources Root，所以引用不到。
#from procedures.threeRule_info import
# 用相对路径引入， .表示当前路径
from .shell_eventID1_info import rule_3_list,tactic_list, technique_list, technique_id_list, eval_phase_list, eval_step_list
from elasticsearch import Elasticsearch
import datetime
import json

es = Elasticsearch('helk-elasticsearch:9200')

for id in range(len(rule_3_list)):

  search_doc_c = {
    "size": 10000,
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "event_id": "1"
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

  res_c = es.search(index="logs-endpoint-winevent-*",body=search_doc_c)

  count =  res_c['hits']['total']['value']

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

  es.index(index="represent_7",body = action, id = id+25)
