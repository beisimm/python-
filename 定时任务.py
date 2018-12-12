from datetime import datetime
from time import sleep


def timed_task(h=0, m=0, s=0):
    def use_logging(func):
        def wrapper():

            curTime = datetime.now()
            print("现在时间", curTime)

            desTime = curTime.replace(hour=h, minute=m, second=s, microsecond=0)
            print("任务时间", desTime)

            delta = desTime - curTime
            print("剩余时间", delta)

            skipSeconds = delta.total_seconds()
            print("下次执行时间%d秒后" % skipSeconds)

            try:
                sleep(skipSeconds)
            except:
                print("你想穿越吗臭小子?!")
            else:
                return func()

        return wrapper

    return use_logging


if __name__ == "__main__":
    @timed_task(22, 46)  # 这里传入时分秒
    def doFunc():
        print("执行任务")


    doFunc()
