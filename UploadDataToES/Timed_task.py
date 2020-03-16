from datetime import datetime
import sched
import time
import os

'''
每个 10 秒打印当前时间。
'''
scheduler = sched.scheduler(time.time, time.sleep)

def timedTask():
    # 初始化 sched 模块的 scheduler 类

    # 增加调度任务
    scheduler.enter(5, 0, timedTask)
    task()
    # 运行任务


# 定时任务
def task():
    print("func2 Time:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    scheduler.enter(0,0, timedTask)
    scheduler.run()