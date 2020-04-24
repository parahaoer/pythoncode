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
          "should": [
            {
              "match_phrase": {
                "param3": "System.Reflection.Assembly.Load"
              }
            },
            {
              "match_phrase": {
                "param3": "[System.Reflection.Assembly]::Load"
              }
            },
            {
              "match_phrase": {
                "param3": "[Reflection.Assembly]::Load"
              }
            },
            {
              "match_phrase": {
                "param3": "System.Reflection.AssemblyName"
              }
            },
            {
              "match_phrase": {
                "param3": "Reflection.Emit.AssemblyBuilderAccess"
              }
            },
            {
              "match_phrase": {
                "param3": "Runtime.InteropServices.DllImportAttribute"
              }
            },
            {
              "match_phrase": {
                "param3": "SuspendThread"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "System.Reflection.Assembly.Load"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "[System.Reflection.Assembly]::Load"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "[Reflection.Assembly]::Load"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "System.Reflection.AssemblyName"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "Reflection.Emit.AssemblyBuilderAccess"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "Runtime.InteropServices.DllImportAttribute"
              }
            },
            {
              "match_phrase": {
                "powershell.scriptblock.text": "SuspendThread"
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
    wb.get_sheet(0).write(rowCount + id, 0,"Suspicious PowerShell Keywords")
wb.save('output.xls')