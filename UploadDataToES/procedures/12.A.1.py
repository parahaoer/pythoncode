from elasticsearch import Elasticsearch
import datetime


es = Elasticsearch('helk-elasticsearch:9200')

search_doc_a = {
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
                "param3": "name=\"Command\"; value=\"route print\""
              }
            }
          ]
        }
      }
    }
  }
}

search_doc_b = {
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
            "powershell.param.value": "route print"
          }
        }
      ]
    }
  }
}

search_doc_c = {
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
            "process_command_line": "*\\\\ROUTE.EXE\" print"
          }
        }
      ]
    }
  }
}

def getTimeStamp(jsonstr):
  return datetime.datetime.strptime(jsonstr['_source']['@timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')

def getTimeDifference(jsonstrA, jsonstrB):
  timeA = getTimeStamp(jsonstrA)
  timeB = getTimeStamp(jsonstrB)
  if timeA.__gt__(timeB):
    return (timeA - timeB).seconds
  else:
    return (timeB-timeA).seconds



res_a = es.search(index="logs-endpoint-winevent-*",body=search_doc_a)
res_b = es.search(index="logs-endpoint-winevent-*",body=search_doc_b)
res_c = es.search(index="logs-endpoint-winevent-*",body=search_doc_c)

list_a =res_a["hits"]["hits"]
list_b =res_b["hits"]["hits"]
list_c =res_c["hits"]["hits"]

count = 0

for a_doc in list_a:
  for b_doc in list_b:
    if(getTimeDifference(a_doc, b_doc) < 1):
      for c_doc in list_c:

        if(getTimeDifference(a_doc, c_doc) < 1 and getTimeDifference(b_doc, c_doc) < 1):
          if(b_doc['_source']['user']['identifier'] == c_doc['_source']['user_sid']):

            count = count + 1
            list_a.remove(a_doc)
            list_b.remove(b_doc)
            list_c.remove(c_doc)
print(count)










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