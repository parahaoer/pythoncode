from mordor_empire.shell_threeRule_info import *
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('output/output.xls')
sheet1 = rb.sheets()[0]
rowCount = sheet1.nrows
wb = copy(rb)

print(rowCount)

for id in range(0, len(rule_1_list)):
    startRow = rowCount + 1

    wb.get_sheet(0).write(rowCount + id*3 + 1, 1, '1')
    wb.get_sheet(0).write(rowCount + id*3 + 1, 2, 'Windows PowerShell')
    wb.get_sheet(0).write(rowCount + id*3 + 1, 3, '800')
    wb.get_sheet(0).write(rowCount + id*3 + 1, 4, 'Pipeline Execution Details')
    wb.get_sheet(0).write(rowCount + id*3 + 1, 5, rule_1_list[id])

    wb.get_sheet(0).write(rowCount + id*3 + 2, 1, '2')
    wb.get_sheet(0).write(rowCount + id*3 + 2, 2, 'Windows PowerShell')
    wb.get_sheet(0).write(rowCount + id*3 + 2, 3, '4103')
    wb.get_sheet(0).write(rowCount + id*3 + 2, 4, 'Executing Pipeline')
    wb.get_sheet(0).write(rowCount + id*3 + 2, 5, rule_2_list[id])

    wb.get_sheet(0).write(rowCount + id*3 + 3, 1, '3')
    wb.get_sheet(0).write(rowCount + id*3 + 3, 2, 'Security')
    wb.get_sheet(0).write(rowCount + id*3 + 3, 3, '4688')
    wb.get_sheet(0).write(rowCount + id*3 + 3, 4, 'Process Creation')
    wb.get_sheet(0).write(rowCount + id*3 + 3, 5, rule_3_list[id])


wb.save('output/output.xls')
    
