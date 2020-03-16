import os

ruleDir = os.getcwd()

#获取文件名后缀
def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shortname,extension) = os.path.splitext(tempfilename);
    return filepath,shortname,extension

def execRule():

    ruleList = os.listdir(ruleDir)
    for file in ruleList:
        _,shortname, extention = jwkj_get_filePath_fileName_fileExt(file)
        if(extention == '.py' and shortname != 'execRules' and shortname != 'Timed_task_3'):
            os.system('python3 ' + file)


if __name__ == "__main__":
    execRule()