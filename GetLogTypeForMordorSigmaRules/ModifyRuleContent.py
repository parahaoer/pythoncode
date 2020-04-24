import os
def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename)
    (shotname,extension) = os.path.splitext(tempfilename)
    #filepath是文件所在的目录（最后没有 /），shotname是去除最后一个. 所得到的文件名
    return filepath,shotname,extension


def modifyFileContent(filePath):

    _,shortname,_ = jwkj_get_filePath_fileName_fileExt(filePath)

    w_str = ""

    for count, line in enumerate(open(filePath, 'r', encoding='gb18030')):

        w_str += line

        if(count ==1):
            w_str += '''
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
'''
        
        if line == 'res = es.search(index="logs-endpoint-winevent-*",body=doc)\n':
            w_str += '''
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
    wb.get_sheet(0).write(rowCount + id, 0,''' + '\"' + shortname + '\"' +''')
wb.save('output.xls')'''

            break

    with open('rule_Modify/'+ shortname +'.py', 'w') as f:
        f.write(w_str)
    
            
ruleDir = './rule'
filelist = os.listdir(ruleDir)

for filename in filelist:
    filePath = ruleDir + '/' +filename

    modifyFileContent(filePath)

