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
              "bool": {
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "7"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wmiclnt.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\WmiApRpl.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wmiprov.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wmiutils.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wbemcomn.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wbemprox.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\WMINet_Utils.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wbemsvc.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\fastprox.dll"
                          }
                        }
                      ]
                    }
                  }
                ]
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
                                  "process_path.keyword": "*\\\\WmiPrvSe.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\WmiAPsrv.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\svchost.exe"
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
    wb.get_sheet(0).write(rowCount + id, 0,"WMI Modules Loaded")
wb.save('output.xls')