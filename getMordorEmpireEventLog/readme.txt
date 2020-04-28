代码亮点：
1、获得正则表达式匹配的字符串，然后按照匹配的字符串分割原来的字符串。
  searchObj = re.search('[0-9]{1,2}\.[A-Z]\.[0-9]', line)
  searchStr = "" if searchObj is None else searchObj.group()
  if searchStr is not "":
      split_list = line.split(searchStr)

2、求列表command_list减去列表command_list_of_three_rules的差集
command_list_left = [command for command in command_list if command not in command_list_of_three_rules]

