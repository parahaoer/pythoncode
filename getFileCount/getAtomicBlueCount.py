
import re

AtomicBlueDetectionTime_list = []
for line in open('resource/AtomicBlueDetection.txt'):
    searchObj = re.search('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', line)
    AtomicBlueDetectionTime = "" if searchObj is None else searchObj.group()

    if AtomicBlueDetectionTime != "":
        print(AtomicBlueDetectionTime)
        AtomicBlueDetectionTime_list.append(AtomicBlueDetectionTime)

print(len(AtomicBlueDetectionTime_list))