import tarfile
import os
dirs = 'F:\\迅雷下载\\mordor-master\\mordor-master\\small_datasets\\windows\\credential_access\\credential_dumping_T1003\\credentials_from_ad'
fname = 'F:\\迅雷下载\\mordor-master\\mordor-master\\small_datasets\\windows\\credential_access\\credential_dumping_T1003\\credentials_from_ad\\empire_dcsync.tar.gz'
def untar(fname, dirs):
    t = tarfile.open(fname)
    t.extractall(path = dirs)

if __name__ == "__main__":
    untar(fname, dirs)