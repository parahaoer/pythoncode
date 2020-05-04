
import re

eqlTime_list = []
for line in open('resource/eqlAnalytics.txt'):
    searchObj = re.search('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', line)
    eqlTime = "" if searchObj is None else searchObj.group()

    if eqlTime != "":
        print(eqlTime)
        eqlTime_list.append(eqlTime)

print(len(eqlTime_list))