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

doc =   {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "5136"
              }
            },
            {
              "match_phrase": {
                "dsobject_attribute_name": "ntSecurityDescriptor"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "match": {
                      "dsobject_attribute_value": "1131f6ad-9c07-11d1-f79f-00c04fc2dcd2"
                    }
                  },
                  {
                    "match": {
                      "dsobject_attribute_value": "*1131f6aa-9c07-11d1-f79f-00c04fc2dcd2*"
                    }
                  },
                  {
                    "match": {
                      "dsobject_attribute_value": "*89e95b76-444d-4c62-991a-0facbeda640c*"
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
    wb.get_sheet(0).write(rowCount + id, 0,"Powerview Add-DomainObjectAcl DCSync AD Extend Right")
wb.save('output.xls')