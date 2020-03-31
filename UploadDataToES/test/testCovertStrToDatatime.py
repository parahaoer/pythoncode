'''
需要用大的时间减去小的时间，才能得到以秒为单位的时间差
如果用小的时间减去大的时间，结果为86399
'''


import datetime

str_p = "2019-05-14T23:16:11.010Z"

str_q = "2019-05-14T23:16:11.011Z"

str_r = "2019-05-14T23:16:09.819Z"

dateTime_p = datetime.datetime.strptime(str_r,'%Y-%m-%dT%H:%M:%S.%fZ')

dateTime_q = datetime.datetime.strptime(str_q,'%Y-%m-%dT%H:%M:%S.%fZ')

if dateTime_p.__gt__(dateTime_q):
    print((dateTime_p - dateTime_q).seconds)
else:
    print((dateTime_q - dateTime_p).seconds)
