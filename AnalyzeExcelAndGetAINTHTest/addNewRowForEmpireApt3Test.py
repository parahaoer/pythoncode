import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

# open the .xlsx file
book = xlrd.open_workbook('resource/excel/对mordor small_dataset的查询 目录_增加.xlsx')
sheet1 = book.sheets()[0]
rule_list = sheet1.col_values(5)
rule_list = [item.strip() for item in rule_list]

# open the .xlsx file
book = xlrd.open_workbook('resource/excel/outputForEmpire.xls')
sheet2 = book.sheets()[0]
sub_rule_list = sheet2.col_values(0)
sub_rule_list = [item.strip() for item in sub_rule_list]

rb = open_workbook('resource/excel/outputResForEmpire.xls')
wb = copy(rb)

for id, rule in enumerate(sub_rule_list):
    #获取rule 的下标, 即在sheet1中的行数
    rowID = rule_list.index(rule)

    desc = sheet1.cell(rowID, 6).value
    tactic = sheet1.cell(rowID, 2).value
    technique = sheet1.cell(rowID, 4).value
    technique_id = sheet1.cell(rowID, 3).value
    procedure = sheet1.cell(rowID, 5).value
    
    point = u'在数据集empire_apt3中检测行为：' + desc + u'。该行为对应ATT&CK中的' + tactic + u'下的'  + technique_id + ' ' + technique + u'下的procudure：' +  procedure

    wb.get_sheet(0).write(id, 0, 74+id)
    wb.get_sheet(0).write(id, 1, rule)
    testItem = u'在数据集empire_apt3中， 检测procedure：' + rule
    wb.get_sheet(0).write(id, 2, testItem)

    wb.get_sheet(0).write(id, 4, point)
wb.save('resource/excel/outputResForEmpire.xls')







