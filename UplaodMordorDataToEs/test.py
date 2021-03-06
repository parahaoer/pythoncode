#!/usr/bin/python
#coding:utf-8

'''
第一步，解压gz文件得到json文件, 该脚本不解压
第二步，修改nxlog数据，该脚本不修改nxlog数据。
第三步，使用该脚本通过kafkacat将json文件。 该脚本只迭代将所有的json温江上传到HELK
'''
import os
import tarfile
#image_path = 'F:\\迅雷下载\\mordor-master\\mordor-master\\small_datasets\\windows'
image_path = os.getcwd()

helk_ip = '172.16.0.16'

# 遍历文件夹及其子文件夹中的文件，并存储在一个列表中

# 输入文件夹路径、空文件列表[]

# 返回 文件列表Filelist,包含文件名（完整路径）

#获取文件名后缀
def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath,shotname,extension

#解压文件
def untar(fname, dirs):
    t = tarfile.open(fname)
    t.extractall(path = dirs)

def get_filelist(dir, Filelist):

    if os.path.isfile(dir):
        Filelist.append(dir)
        filepath, shortname, extention = jwkj_get_filePath_fileName_fileExt(dir)
        # if extention == '.gz':
        #     if(not os.path.exists(filepath + shortname + "_[0-9]{4}_*.py")):
        #         untar(dir, filepath)
        if extention == '.json':
            shellcode = 'kafkacat -b ' + helk_ip + ':9092 -t winlogbeat -P -l ' + dir
            os.system(shellcode)
            print(shellcode)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist

if __name__ == '__main__':
    list = get_filelist(image_path, [])

    for e in list:
        print(e)
    print(len(list))
