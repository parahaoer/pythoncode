w_str = ""

for count, line in enumerate(open("test.py",'r', encoding = 'utf-8')):
    if(count ==0):
        w_str = line
        continue
    if(count ==1):
        line = "class testClass():\r\n"
    else:
        line = '\t' + line

    w_str += line

with open("test.py",'w') as f:
    f.write(w_str)