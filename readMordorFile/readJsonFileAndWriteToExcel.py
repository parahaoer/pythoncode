import json

from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('LogAnalitic.xlsx')
wb = copy(rb)

i=0
for line in open(r'covenant_dcsync_all_2019-10-27064128.json'):
    d = json.loads(line)
    timestamp = d['@timestamp']
    wb.get_sheet(0).write(i, 0, i)
    wb.get_sheet(0).write(i, 1, timestamp)
    wb.save('output.xls')
    i = i + 1

print(i)