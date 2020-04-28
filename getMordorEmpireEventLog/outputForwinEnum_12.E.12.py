from mordor_empire.winEnum_12_E_12_info import *
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('output/output.xls')
sheet1 = rb.sheets()[0]
rowCount = sheet1.nrows
wb = copy(rb)

print(rowCount)

for id in range(0, len(rule_3_list)):
    startRow = rowCount + 1
    wb.get_sheet(0).write(rowCount + id*1 + 1, 0, 'usemodule situational_awareness/host/winenum')
    wb.get_sheet(0).write(rowCount + id*1 + 1, 1, '1')
    wb.get_sheet(0).write(rowCount + id*1 + 1, 2, 'Windows PowerShell')
    wb.get_sheet(0).write(rowCount + id*1 + 1, 3, '800')
    wb.get_sheet(0).write(rowCount + id*1 + 1, 4, 'Pipeline Execution Details')
    wb.get_sheet(0).write(rowCount + id*1 + 1, 5, rule_3_list[id])



wb.save('output/output.xls')
    
