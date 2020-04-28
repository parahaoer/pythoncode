
def getCommandListOfThreeRules():
    command_list_of_three_rules = []
    for line in open('resource/CommandOfThreeRules.txt',encoding='utf-8'):
        if line.strip() is "":
            continue
        command_list_of_three_rules.append(line.strip())
    
    return  command_list_of_three_rules


def getCommandCount():
    command_list_of_three_rules = []
    for line in open('resource/command.txt',encoding='utf-8'):
        if line.strip() is "":
            continue
        command_list_of_three_rules.append(line.strip())
    print(len(command_list_of_three_rules))
    return  command_list_of_three_rules

getCommandCount()