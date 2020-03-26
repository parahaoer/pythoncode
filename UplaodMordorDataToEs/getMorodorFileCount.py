import os

class GetMordorFileCount:
    count = 0

    def jwkj_get_filePath_fileName_fileExt(slef, filename):
        (filepath, tempfilename) = os.path.split(filename);
        (shotname, extension) = os.path.splitext(tempfilename);
        # filepath是文件所在的目录（最后没有 /），shotname是去除最后一个. 所得到的文件名
        return filepath, shotname, extension

    def get_filelist(self,dir, Filelist):

        if os.path.isfile(dir):
            Filelist.append(dir)
            filepath, shortname, extention = self.jwkj_get_filePath_fileName_fileExt(dir)
            if extention == '.gz':
                getMordorFileCount.count = getMordorFileCount.count + 1

        elif os.path.isdir(dir):
            for s in os.listdir(dir):

                newDir = os.path.join(dir, s)
                self.get_filelist(newDir, Filelist)
        return Filelist
getMordorFileCount = GetMordorFileCount()
getMordorFileCount.get_filelist(".", [])
print(getMordorFileCount.count)