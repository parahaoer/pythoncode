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
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\mshta.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\powershell.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\rundll32.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\cscript.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\wscript.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\wmiprvse.exe"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\schtasks.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\nslookup.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\certutil.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\bitsadmin.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\mshta.exe"
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
                          "wildcard": {
                            "process_current_directory.keyword": "*\\\\ccmcache\\\\*"
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
    wb.get_sheet(0).write(rowCount + id, 0,"Windows Shell Spawning Suspicious Program")
wb.save('output.xls')