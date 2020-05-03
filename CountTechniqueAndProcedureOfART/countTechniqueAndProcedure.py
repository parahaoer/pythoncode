import docx
import re

doc = docx.Document('resource/part2.docx')

paragraphs = doc.paragraphs

technique_dict = {}
technique = ""
technique_procedure_dict = {}
for paragraph in paragraphs:

    # 如果段落内容是超链接， para_text 将是空串。
    # 去除超链接：选中全文后，快捷键Ctrl+6 
    para_text = paragraph.text.strip()

    if(paragraph.style.name == 'Heading 3'):
        searchObj = re.search('T[0-9]{4}', para_text)
        technique = "" if searchObj is None else searchObj.group()
        technique = technique.strip()
        technique_dict[technique] = technique_dict.get(technique, 0) + 1 

    
    elif(paragraph.style.name == 'Heading 5'):
        
        if para_text not in  technique_procedure_dict.get(technique, []):
            
            procedure_list =  technique_procedure_dict.setdefault(technique,[])
            procedure_list.append(para_text)

print(len(technique_dict.keys()))

procedure_count = 0
for tech in technique_procedure_dict.keys():
    procedure_list = technique_procedure_dict.get(tech)
    for procedure in procedure_list:
        procedure_count = procedure_count + 1
print(procedure_count)

with open('resource/my_file.csv', 'w') as f:
    for technique, procedure_list in technique_procedure_dict.items():
        for procedure in procedure_list:
            # 每一个 technique, procedure 对 占一行
            f.write('{0},{1}\n'.format(technique, procedure))
    # [f.write('{0},{1}\n'.format(key, value)) for key, value in technique_procedure_dict.items()]



