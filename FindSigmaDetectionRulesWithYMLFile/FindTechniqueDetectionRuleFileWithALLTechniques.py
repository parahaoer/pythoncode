import os
import yaml
import sys

pwd = '/home/atomic-threat-coverage/detection_rules/sigma/rules/'

#获取当前工作目录
src = os.getcwd()

#修改工作路径
os.chdir(pwd)


list = ['t1191', 't1196', 't1170', 't1086', 't1117', 't1085', 't1053', 't1064', 't1127', 't1047', 't1028']
for technique in list:
    mycmdStr = ' grep -r ' + technique

    mycmd = os.popen(mycmdStr)

    lines = mycmd.readlines()

    for line in lines:
        #按不定空格分隔字符串
        str_list = line.split()
        #获取文件路径
        #print(str_list[0])

        #加载文件 ##[:-1]用来去除字符串最后一个无用的:
        f = open(pwd + str_list[0][:-1], encoding="utf-8")
        print(pwd + str_list[0][:-1])
        try:
            x = yaml.load(f)
        except yaml.composer.ComposerError:
            continue

        #将查找到的Rules 写入到对应technique.txt中
        f = open(src + '/' + technique + '.txt', 'at')
        f.write(x['title'] + '\r\n')
        f.close()
        print(x['title'])

