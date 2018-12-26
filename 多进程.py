import os
from multiprocessing import Process
import time


def run_proc():
    """子进程要执行的代码"""
    print('子进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号

    while True:
        print("----2----")
        time.sleep(1)


if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号

    p = Process(target=run_proc)
    p.start()
    while True:
        print("----1----")
        time.sleep(1)
