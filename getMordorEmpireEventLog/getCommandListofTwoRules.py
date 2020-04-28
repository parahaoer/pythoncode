from getCommandList import getCommandList
from getCommandListOfThreeRules import getCommandListOfThreeRules
command_list = getCommandList()

command_list_of_three_rules = getCommandListOfThreeRules()

command_list_left = [command for command in command_list if command not in command_list_of_three_rules]

for item in command_list_left:
    print(item)


