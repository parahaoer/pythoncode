from elasticsearch import Elasticsearch


import os
import sys
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
sys.path.append(os.getcwd())
from helk_info import HELK_IP

rb = open_workbook('output.xls')
wb = copy(rb)
sheet1 = rb.sheets()[0]
rowCount = sheet1.nrows
print(rowCount)
es = Elasticsearch(HELK_IP + ':9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "10"
              }
            },
            {
              "match_phrase": {
                "process_target_path": "C:\\windows\\system32\\lsass.exe"
              }
            },
            {
              "match_phrase": {
                "process_granted_access": "4112"
              }
            },
            {
              "bool": {
                "must_not": [
                  {
                    "bool": {
                      "must": [
                        {
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\wmiprvse.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\taskmgr.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\procexp64.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\procexp.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\lsm.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\csrss.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\wininit.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\vmtoolsd.exe"
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
          ]
        }
      }
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

res_list = res['hits']['hits']

log_type = set([])
for item in res_list:
    _index = item['_index']
    if 'security' in _index:
        log_type.add('security')
    elif 'sysmon' in _index:
        log_type.add('sysmon')
    elif 'powershell' in _index:
        log_type.add('powershell')
    elif 'wmiactivity' in _index:
        log_type.add('wmiactivity')

log_type_list = list(log_type)

for id in range(0, len(log_type_list)):
    wb.get_sheet(0).write(rowCount + id, 1, log_type_list[id])
    wb.get_sheet(0).write(rowCount + id, 0,"Mimikatz Detection LSASS Access")
wb.save('output.xls')