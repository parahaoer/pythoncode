count=-1
for count, line in enumerate(open("WriteOnedata.py",'r', encoding = 'utf-8')):
    if(count == 18) :
        print(line[:-2] + ', id =3)\n')
count+=1
print(count)
