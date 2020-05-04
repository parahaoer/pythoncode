import os

def get_filelist(dir, Filelist):

    if os.path.isfile(dir):
        Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist

if __name__ == '__main__':
    image_path = "C:\\gitRepo\\sigma\\rules"
    list = get_filelist(image_path, [])
    print(len(list))
    for e in list:
        print(e)
