import  re

def modifyFileData(filePath, index):

    w_str = ""

    #for count, line in enumerate(open(filePath,'r', encoding = 'utf-8')):
    for count, line in enumerate(open(filePath, 'r', encoding='gb18030')):
        if re.search('tatic', line):
            line = re.sub('tatic', 'tactic', line)

        if re.search('Tatic', line):
            line = re.sub('Tatic', 'Tactic', line)

        # elif re.search('Count', line):
        #     line = re.sub('Count', 'EventCount', line)

        elif re.search('rule_name', line):
            line = re.sub('rule_name', 'procedure', line)

        elif re.search('Rule', line):
            line = re.sub('Rule', 'Procedure', line)

        elif re.search('represent_6', line):
            line = re.sub('represent_6', 'represent_5', line)

        if re.search('es.index', line):
            line = line[:-2] + ', id = ' + str(index) + ')\n'

        w_str += line

    with open(filePath, 'w') as f:
        f.write(w_str)