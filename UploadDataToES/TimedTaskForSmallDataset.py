import sched
import time
import os
from execRules import execRule

'''
每隔5s 执行 1次execRule函数
'''

dir = os.getcwd()

def timedTask():
    # 初始化 sched 模块的 scheduler 类
    scheduler = sched.scheduler(time.time, time.sleep)
    # 增加调度任务
    scheduler.enter(5, 0, timedTask)
    task()
    # 运行任务
    scheduler.run()

# 定时任务
def task():
    execRule("procedures")

if __name__ == '__main__':
    timedTask()