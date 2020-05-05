import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

url_step_dict = {}
# step  url 建立关系
book = xlrd.open_workbook('resource/apt3_mordor_playbook_标注sigma规则_补充.xlsx')
sheet1 = book.sheets()[0]
for rowNum in range(1, sheet1.nrows):
    step = sheet1.cell(rowNum, 0).value
    url = sheet1.cell(rowNum, 13).value
    print(url)
    url = url.strip()
    if(url != ""):
        url_step_dict[url] = step.strip()



rule_url_dict = {}
# rule url 建立关系
book2 = xlrd.open_workbook('resource/对mordor small_dataset的查询 目录_增加.xlsx')
sheet2 = book2.sheets()[0]
for rowNum in range(1, sheet2.nrows):
    rule = sheet2.cell(rowNum, 5).value
    # print(rule)
    url = sheet2.cell(rowNum, 8).value
    rule_url_dict[rule.strip()] = url.strip()


# 根据rule 找 step

rb = open_workbook('resource/对empire的检测结果.xls')
wb = copy(rb)
sheet3 = rb.sheets()[0]

for rowNum in range(sheet3.nrows):
    rule = sheet3.cell(rowNum, 0).value

    url = rule_url_dict[rule]
    try:
        step = url_step_dict[url]
    except KeyError:
        continue

    wb.get_sheet(0).write(rowNum, 3, step)

wb.save('resource/output.xls')

