import os
def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    #filepath是文件所在的目录（最后没有 /），shotname是去除最后一个. 所得到的文件名
    return filepath,shotname,extension