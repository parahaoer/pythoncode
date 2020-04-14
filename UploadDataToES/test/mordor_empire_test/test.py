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
                "event_id": "600"
              }
            },
            {
              "match_phrase": {
                "powershell.providername": "Registry"
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
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "600"
              }
            },
            {
              "match_phrase": {
                "powershell.providername": "Alias"
              }
            }
          ]
        }
      }
    }
  }
}

search_doc_c = {
  "size": 10000,
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "600"
              }
            },
            {
              "match_phrase": {
                "powershell.providername": "Environment"
              }
            }
          ]
        }
      }
    }
  }
}

search_doc_d = {
  "size": 10000,
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "600"
              }
            },
            {
              "match_phrase": {
                "powershell.providername": "FileSystem"
              }
            }
          ]
        }
      }
    }
  }
}

search_doc_e = {
  "size": 10000,
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "600"
              }
            },
            {
              "match_phrase": {
                "powershell.providername": "Function"
              }
            }
          ]
        }
      }
    }
  }
}

search_doc_f = {
  "size": 10000,
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "600"
              }
            },
            {
              "match_phrase": {
                "powershell.providername": "Variable"
              }
            }
          ]
        }
      }
    }
  }
}

search_doc_g = {
  "size": 10000,
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "400"
              }
            }
          ]
        }
      }
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
res_c = es.search(index="logs-endpoint-winevent-*",body=search_doc_c)
res_d = es.search(index="logs-endpoint-winevent-*",body=search_doc_d)
res_e = es.search(index="logs-endpoint-winevent-*",body=search_doc_e)
res_f = es.search(index="logs-endpoint-winevent-*",body=search_doc_f)
res_g = es.search(index="logs-endpoint-winevent-*",body=search_doc_g)

list_a =res_a["hits"]["hits"]
list_b =res_b["hits"]["hits"]
list_c =res_c["hits"]["hits"]
list_d =res_d["hits"]["hits"]
list_e =res_e["hits"]["hits"]
list_f =res_f["hits"]["hits"]
list_g =res_g["hits"]["hits"]

# 对list_a、list_b、list_c 列表分别按照时间先后排序
list_a.sort(key=cmp_to_key(cmp_datetime))
list_b.sort(key=cmp_to_key(cmp_datetime))
list_c.sort(key=cmp_to_key(cmp_datetime))
list_d.sort(key=cmp_to_key(cmp_datetime))
list_e.sort(key=cmp_to_key(cmp_datetime))
list_f.sort(key=cmp_to_key(cmp_datetime))
list_g.sort(key=cmp_to_key(cmp_datetime))
count = 0

list_compare = [list_a, list_b, list_c, list_d, list_e, list_f, list_g]



  for id in range(len(list_a)):
    for i in range(len(list_compare)):
      for j in range(i+1, len(list_compare)):
        if(getTimeDifference(list_compare[i][id], list_compare[j][id]) <= 1):
          continue
        else
          break
        

          

    if(getTimeDifference(list_a[id], ))
for a_doc in list_a:
  for b_doc in list_b:
    if(getTimeDifference(a_doc, b_doc) <= 1):
      for c_doc in list_c:

        if(getTimeDifference(a_doc, c_doc) <= 1 and getTimeDifference(b_doc, c_doc) <= 1):
          for
            count = count + 1
            list_a.remove(a_doc)
            list_b.remove(b_doc)
            list_c.remove(c_doc)
print(count)

tactic = "Lateral Movement"
technique = "Remote File Copy"
tech_code = "T1105"
eval_phase = "Lateral Movemet"
eval_step = "16.E.1"

action = {
  "Tactic": tactic,
  "Technique": technique,
  "Tech_code": tech_code,
  "EvalStep": eval_step,
  "EvalPhase": eval_phase,
  "EventCount": count,
}

