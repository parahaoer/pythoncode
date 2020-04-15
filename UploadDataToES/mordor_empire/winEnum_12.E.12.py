from functools import cmp_to_key
# pycharm 默认该项目的根目录为sources Root，所以引用不到。
#from procedures.threeRule_info import
# 用相对路径引入， .表示当前路径
from .winEnum_12_E_12_info import rule_3_list,tactic_list, technique_list, technique_id_list, eval_phase_list, eval_step_list
from elasticsearch import Elasticsearch
import datetime
import json

es = Elasticsearch('helk-elasticsearch:9200')

for id in range(len(rule_3_list)):

  search_doc_c = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "param1": ""
              }
            }
          ]
        }
      }
    }
  }
}

  search_doc_c["query"]["constant_score"]["filter"]["bool"]["must"][0]["match_phrase"]["param1"] = rule_3_list[id]

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

  es.index(index="represent_7",body = action, id = id+35)










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