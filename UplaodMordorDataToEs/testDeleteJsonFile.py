#!/usr/bin/python
#coding:utf-8
import os
import tarfile
#image_path = 'F:\\迅雷下载\\mordor-master\\mordor-master\\small_datasets\\windows'
image_path = os.getcwd()

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
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
        filepath, _, extention = jwkj_get_filePath_fileName_fileExt(dir)
        if extention == '.gz':
            untar(dir, filepath)
        if extention == '.json':
            shellcode = 'kafkacat -b 10.25.23.5:9092 -t winlogbeat -P -l ' + dir
            os.system(shellcode)
            print(shellcode)
            #将输入导入后，删除json文件
            os.remove(dir)
        # # 若只是要返回文件文，使用这个
        # Filelist.append(os.path.basename(dir))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
     #              # if s == "xxx":
        #                   # continue
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist

if __name__ == '__main__':
    list = get_filelist(image_path, [])
    print(len(list))
    for e in list:
        print(e)