import os
import yaml
import sys

def output(filepath, technique, filename, src):
    outputdir = src + '/' + technique
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    sigmacStr = 'python3 ../tools/sigmac -t es-dsl -c helk ' + filepath + ' -o' + outputdir + '/' + filename + '.txt'

    print('sigmacstr' + sigmacStr)
    os.popen(sigmacStr)

def getFileName(filepath):
    filename = filepath.split('/')[-1]
    return filename[:-4]

if __name__ == '__main__':
    pwd = '/home/atomic-threat-coverage/detection_rules/sigma/rules/'

    # 获取当前工作目录
    src = os.getcwd()

    # 修改工作路径
    os.chdir(pwd)

    # sys.argv[1]通过命令行接收T
    technique = sys.argv[1]
    mycmdStr = ' grep -r ' + technique

    mycmd = os.popen(mycmdStr)

    fw = open(src + '/' + technique + '.txt', 'at')
    lines = mycmd.readlines()

    for line in lines:
        # 按不定空格分隔字符串
        str_list = line.split()
        # 获取文件路径
        # print(str_list[0])
        # 加载文件 ##[:-1]用来去除字符串最后一个无用的:
        filepath = pwd + str_list[0][:-1]

        filename = getFileName(filepath)

        f = open(filepath, encoding="utf-8")
        print('filepath' + filepath)
        try:
            x = yaml.load(f)
        except yaml.composer.ComposerError:
            continue

        title = x['title']
        # 将查找到的Rules 写入到对应technique.txt中

        fw.write(title + '\r\n')
        print('title' + title)

        output(filepath, technique, filename, src)
    fw.close()


