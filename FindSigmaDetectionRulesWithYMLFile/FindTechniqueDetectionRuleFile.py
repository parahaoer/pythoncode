import os

os.chdir('/home/atomic-threat-coverage/detection_rules/sigma/rules')

mycmdStr = ' grep -r T1086'

mycmd = os.popen(mycmdStr)

lines = mycmd.readlines()

print(lines[0])