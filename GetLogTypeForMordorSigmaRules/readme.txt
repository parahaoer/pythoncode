第一步， 运行ModifyRuleContent.py文件， 修改rule目录下原始的rule规则到rule_Modify目录下。
       在修改后的rule规则文件中， 遍历返回结果列表res_list，获得每一个hit的索引名，判断该索引是sysmon、security、powershell等日志。并写入到output.xls文件中。

第二步，运行outputLogTypeExcel.py文件， 运行rule_Modify中的每一个rule文件。 将规则名、日志类型信息依次按行追加写入output.xls文件中。
