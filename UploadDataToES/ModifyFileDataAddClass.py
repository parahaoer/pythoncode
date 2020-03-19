import re
from getFileShortName import jwkj_get_filePath_fileName_fileExt

def modifyFileDataAddClass(filepath):
    w_str = ""

    for count, line in enumerate(open(filepath, 'r', encoding = 'utf-8')):
        if(count ==0):
            w_str = line
            continue
        if(count ==1):
            file_name = jwkj_get_filePath_fileName_fileExt(filepath)
            line = "class " + file_name + "():\r\n"
            line = line + "\tTotalCount = 0"
        else:
            line = '\t' + line


        w_str += line

    with open(filepath,'w') as f:
        f.write(w_str)