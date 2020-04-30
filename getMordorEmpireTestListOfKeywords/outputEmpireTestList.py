from xlrd import open_workbook
from xlutils.copy import copy
import xlrd

# open the .xlsx file
book = xlrd.open_workbook('resource/modor empire 检测关键字.xls')
sheet1 = book.sheets()[0]

rb = open_workbook('resource/output.xls')
wb = copy(rb)

id = 1
for rowNum in range(1, sheet1.nrows):
    eval_step = sheet1.cell(rowNum, 0).value
    command = sheet1.cell(rowNum,1).value
    if(eval_step is not ""):

        wb.get_sheet(0).write(id, 1, u'Empire APT3 Eval Step：' + eval_step)
        wb.get_sheet(0).write(id, 2, u'检测命令' + command + u'的执行')

        point = ""
        if(rowNum + 1 == sheet1.nrows) :
            break
        # 3 规则
        if(sheet1.cell(rowNum+1,0).value is "" and sheet1.cell(rowNum+2,0).value is "" and sheet1.cell(rowNum+3,0).value is "" and sheet1.cell(rowNum+4,0).value is not ""):
            point = u'检测规则1：检测event_id=800，且event_data.param3包含字符串：' +   sheet1.cell(rowNum,6).value + '\n' + \
                    u'检测规则2：检测event_id=4103，且powershell.param.value字段值为' +   sheet1.cell(rowNum+1,6).value + '\n'
            
            event_id = sheet1.cell(rowNum+2,4).value
            if event_id == '4688':
                point += u'检测规则3：检测event_id=4688，且process_command_line为' +   sheet1.cell(rowNum+2,6).value + '\n'
            elif event_id == 11:
                point += u'检测规则3：检测event_id=11，且file_name为' +   sheet1.cell(rowNum+2,6).value + '\n'
                    
            point += u'约束条件： 3条规则返回记录的时间戳在1s内'
        
        # 2 规则
        if(sheet1.cell(rowNum+1,0).value is "" and sheet1.cell(rowNum+2,0).value is "" and sheet1.cell(rowNum+3,0).value is not "" ):
            point = u'检测规则1：检测event_id=800，且event_data.param3包含字符串：' +   sheet1.cell(rowNum,6).value + '\n' + \
                    u'检测规则2：检测event_id=4103，且powershell.param.value字段值为' +   sheet1.cell(rowNum+1,6).value + '\n' + \
                    u'约束条件： 2条规则返回记录的时间戳在1s内'
        
        
        # 1 规则
        if(sheet1.cell(rowNum+1,0).value is "" and sheet1.cell(rowNum+2,0).value is not ""):
            
            event_id = sheet1.cell(rowNum, 4).value 
            if event_id == '800':
                point = u'检测event_id=800，且event_data.param3包含字符串：' +   sheet1.cell(rowNum,6).value
            elif event_id == 1:
                point = u'检测event_id=1，且process_command_line：' +   sheet1.cell(rowNum,6).value
                

        
        wb.get_sheet(0).write(id, 4, point)
        id = id + 1

wb.save('resource/output.xls')

        


