import xlrd

# open the .xls file
book = xlrd.open_workbook('resource/helk dashboard visualization_补充完整.xlsx')

sheet1 = book.sheets()[0]


dashboard = ""

for rowNum in range(1, sheet1.nrows):

    curr_dashboard = sheet1.cell(rowNum, 0).value
    if(curr_dashboard is not ""):
        dashboard = curr_dashboard
        with open("resource/output.txt", "at", encoding="utf-8") as file:
            file.write(dashboard + '\n')
    
    visualization = sheet1.cell(rowNum, 1).value
    visualization_type = sheet1.cell(rowNum, 2).value
    description = sheet1.cell(rowNum, 3).value

    if(visualization is not ""):
        with open("resource/output.txt", "at", encoding="utf-8") as file: 
            file.write(visualization + '\n')
            file.write('该visualization的类型为' + visualization_type + ',其作用是' + description + '\n')


