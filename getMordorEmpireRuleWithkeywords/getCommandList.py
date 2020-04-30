import xlrd
import re
from xlrd import open_workbook
from xlutils.copy import copy

def getCommandList(step_list, command_list, filepath):
    for line in open(filepath, encoding='utf-8'):
        # print(re.findall('[0-9]{1,2}\.[A-Z]\.[0-9]', line))

        searchObj = re.search('[0-9]{1,2}\.[A-Z]\.[0-9]', line)
        searchStr = "" if searchObj is None else searchObj.group()
        if searchStr is not "":
            split_list = line.split(searchStr)
            step_list.append(searchStr)
            command_list.append(split_list[-1].strip())

    return step_list, command_list

step_list = []
command_list = []

filepath = 'resource/target_shell'


step_list, command_list = getCommandList(step_list, command_list, filepath)

filepath2 = 'resource/target_cmd'

step_list, command_list = getCommandList(step_list, command_list, filepath2)
print(step_list)

rb = open_workbook(u'resource/modor empire 检测关键字.xls')
wb = copy(rb)
sheet1 = rb.sheets()[0]
command_col = sheet1.col_values(1)

rowNumAndCommandTupleList = [(rowNum,command) for rowNum, command in enumerate(command_col) if command in command_list]
for id, rowNumAndCommandTuple in enumerate(rowNumAndCommandTupleList):
    rowNum = rowNumAndCommandTuple[0]
    command = rowNumAndCommandTuple[1]
    step_id = command_list.index(command)
    
    wb.get_sheet(0).write(rowNum, 0, step_list[step_id])
wb.save(u'resource/modor empire 检测关键字.xls')


