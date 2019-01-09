import stackless  # 导入stackless模块
import queue  # 导入Queue模块


def Producer(i):  # 定义生产者

    global queue  # 声明为全局Queue对象
    queue.put(i)  # 向队列中添加数据
    print('Producer', i, 'add', i)


def Consumer():  # 定义消费者

    global queue


    i = queue.get()  # 从队列中取出数据
    print('Consumer', i, 'get', i)
queue = queue.Queue()  # 生成队列对象
for i in range(10000):
    stackless.tasklet(Producer)(i)  # 添加生产者任务
for i in range(10000):
    stackless.tasklet(Consumer)()  # 添加消费者任务
stackless.run()
# print(ts,ts2)
