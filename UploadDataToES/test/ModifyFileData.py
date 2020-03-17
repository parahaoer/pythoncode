import  re

w_str = ""

for count, line in enumerate(open("../rule/WMI Spawning Windows PowerShell.py",'r', encoding = 'utf-8')):

    if re.search('tatic', line):
        line = re.sub('tatic', 'tactic', line)

    if re.search('Tatic', line):
        line = re.sub('Tatic', 'Tactic', line)

    if re.search('Count', line):
        line = re.sub('Count', 'EventCount', line)

    if re.search('rule_name', line):
        line = re.sub('rule_name', 'procedure', line)

    if re.search('Rule', line):
        line = re.sub('Rule', 'Procedure', line)

    if re.search('es.index', line):
        line = line[:-2] + ', id =3)\n'

    w_str += line

with open("../rule/WMI Spawning Windows PowerShell.py",'w') as f:
    f.write(w_str)