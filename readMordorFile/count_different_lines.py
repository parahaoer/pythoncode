import json

s1 = set([])
i=0

for line in open(r'covenant_dcsync_all_2019-10-27064128.json'):
    s1.add(line)
    i = i + 1
print(i)
print(len(s1))