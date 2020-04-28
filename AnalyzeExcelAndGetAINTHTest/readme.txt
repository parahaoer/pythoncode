rb = open_workbook('resource/excel/forOutput.xls')
wb = copy(rb)

当向wb中写入数据时，如果将wb保存到不是resource/excel/forOutput.xls同一个文件中，可能内容并不完整。 原因可能是写入数据中含有中文。

亮点代码：
1、获取excel表格某一列元素的列表
sheet2.col_values(0)

2、遍历列表中的元素并获得其下标：
for id, rule in enumerate(sub_rule_list)

3、匹配例如： 12、 字样的字符串。 re.match 是 从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回None
 re.match('^' + str(id) + u'、\\s*$' , paragraph.text)



