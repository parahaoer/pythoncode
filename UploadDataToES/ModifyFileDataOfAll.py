import os
from ModifyFileData import modifyFileData

ruleDir = './rule/'

id = 0
ruleList = os.listdir(ruleDir)
for file in ruleList:
    filepath = ruleDir + file
    modifyFileData(filepath, id)
    id = id + 1

