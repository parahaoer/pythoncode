import json
i=0
j =0
for line in open(r'covenant_dcsync_all_2019-10-27064128.json'):
    d = json.loads(line)
    task = d['winlog']['task']
    if(task == 'Process accessed (rule: ProcessAccess)'):
        j = j + 1
    i = i + 1
print(i)

print(j)