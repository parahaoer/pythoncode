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

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "param3.keyword": "*DumpCreds*"
                    }
                  },
                  {
                    "wildcard": {
                      "param3.keyword": "*invoke-mimikatz*"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must": [
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "param3.keyword": "*rpc*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*token*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*crypto*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*dpapi*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*sekurlsa*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*kerberos*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*lsadump*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*privilege*"
                          }
                        },
                        {
                          "wildcard": {
                            "param3.keyword": "*process*"
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
                            "param3.keyword": "*::*"
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
    wb.get_sheet(0).write(rowCount + id, 0,"Mimikatz Command Line")
wb.save('output.xls')