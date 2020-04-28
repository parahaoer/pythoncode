import re

def getCommandList():
    command_list = []
    for line in open('resource/target_shell',encoding='utf-8'):
        # print(re.findall('[0-9]{1,2}\.[A-Z]\.[0-9]', line))

        searchObj = re.search('[0-9]{1,2}\.[A-Z]\.[0-9]', line)
        searchStr = "" if searchObj is None else searchObj.group()
        if searchStr is not "":
            split_list = line.split(searchStr)
            command_list.append(split_list[-1].strip())

    for item in command_list:
        print(item + '\n')
    return command_list


