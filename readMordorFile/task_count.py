import json
i=0
s1 = set([])
for line in open(r'covenant_dcsync_all_2019-10-27064128.json'):
    d = json.loads(line)
    task = d['winlog']['task']
    s1.add(task)
    i = i + 1
print(i)
print(len(s1))
for task in s1:
    print(task)