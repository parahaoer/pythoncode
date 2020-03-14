import os
def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    #filepath是文件所在的目录（最后没有 /），shotname是去除最后一个. 所得到的文件名
    return filepath,shotname,extension

fname = 'F:\\迅雷下载\\mordor-master\\mordor-master\\small_datasets\\windows\\credential_access\\credential_dumping_T1003\\credentials_from_ad\\empire_dcsync.tar.gz'
# shotname为empire_dcsync.tar， extension为 .gz
print(jwkj_get_filePath_fileName_fileExt(fname))

fname2 = fname = 'F:\\迅雷下载\\mordor-master\\mordor-master\\small_datasets\windows\\discovery\\permissions_group_discovery_T1069\\empire_bloodhound_2019-03-19031847.json'
print(jwkj_get_filePath_fileName_fileExt(fname2))
