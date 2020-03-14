import os

def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath,shotname,extension

def get_filelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
        filepath, shortname, extention = jwkj_get_filePath_fileName_fileExt(dir)
        if extention == '.gz':
            #python字符串切片格式[start:end:step], [:end]是从开头提取到end - 1，[:-4]表示从开头提取到倒数第4个（排除倒数第4个）
            #print (filepath + '/' + shortname[:-4])
            if (os.path.exists(filepath + '/' + shortname[:-4] + "_[0-9][0-9][0-9][0-9]-*.json")):
                print (filepath + '/' + shortname[:-4] + "_[0-9]{4}_*.json")
            if (os.path.exists(filepath + '/' + shortname + ".gz")):
                print (filepath + '/' + shortname[:-4] + "_[0-9]{4}_*.json")

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist


if __name__ == '__main__':
    list = get_filelist('.', [])
