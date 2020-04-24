import os
fileDir = './rule_Modify'
filelist = os.listdir(fileDir)

for filename in filelist:
    filePath = fileDir + '/' + filename
    os.system('python ' +'\"' +filePath + '\"')