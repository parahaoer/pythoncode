import sched
import time
import os

'''
每个 10 秒打印当前时间。
'''
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
    os.system('sh execPythonfile.sh')

if __name__ == '__main__':
    timedTask()