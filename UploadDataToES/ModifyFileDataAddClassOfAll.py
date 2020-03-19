import os
from ModifyFileDataAddClass import modifyFileDataAddClass


ruleDir = './procedures_2/'

ruleList = os.listdir(ruleDir)
for file in ruleList:
    filepath = ruleDir + file
    modifyFileDataAddClass(filepath)

