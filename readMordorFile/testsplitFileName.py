import os
file_path = 'abc'

str = '\\'
print(str in file_path)

filepath,fullflname = os.path.split(file_path)
fname,ext = os.path.splitext(fullflname)
print(fullflname)
