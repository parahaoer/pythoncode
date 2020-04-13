import xlrd

# open the .xls file
book = xlrd.open_workbook('../resource/apt3_mordor_playbook.xlsx')

sheet1 = book.sheets()[0]

step_set = set([])

for id in range(1, sheet1.nrows):
    #print(sheet1.cell(id, 0).value)
    step_set.add(sheet1.cell(id, 0).value)

step_with_ruleFinished_set = set([])

for line in open(r'../resource/APT3Step_with_ruleFinished.txt'):
    step_with_ruleFinished_set.add(line.strip())

step_without_rule_set = step_set - step_with_ruleFinished_set

with open('../resource/apt3Step_without_rule.txt', 'w') as f:
    for line in step_without_rule_set:
        f.write(line+'\n')


