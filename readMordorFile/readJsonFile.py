import json

# with open('covenant_dcsync_all_2019-10-27064128.json', encoding='utf-8') as f:
#     line = f.readline()
#
#     d = json.loads(line)
#     timestamp = d['@timestamp']
#
#
#     print(timestamp)
i=0

for line in open(r'covenant_dcsync_all_2019-10-27064128.json'):
    d = json.loads(line)
    provider_name = d['winlog']['provider_name']
    i = i + 1
    print(provider_name)
print(i)