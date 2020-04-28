代码亮点：
1、获得正则表达式匹配的字符串，然后按照匹配的字符串分割原来的字符串。
  searchObj = re.search('[0-9]{1,2}\.[A-Z]\.[0-9]', line)
  searchStr = "" if searchObj is None else searchObj.group()
  if searchStr is not "":
      split_list = line.split(searchStr)

2、
