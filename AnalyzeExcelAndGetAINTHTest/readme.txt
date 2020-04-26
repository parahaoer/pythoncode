rb = open_workbook('resource/excel/forOutput.xls')
wb = copy(rb)

当向wb中写入数据时，如果将wb保存到不是resource/excel/forOutput.xls同一个文件中，可能内容并不完整。 原因可能是写入数据中含有中文。


