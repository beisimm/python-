'''
Queue 它是一个线程安全的队列
当一个县城get数据时,其他线程操作queue时候加锁
'''

# 导入协程池
from gevent.pool import Pool
import gevent.monkey
gevent.monkey.patch_all()
import time
from queue import Queue
import requests
from lxml import etree


class QiubaiSpider(object):
    def __init__(self):
        self.base_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent": "Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        self.url_queue = Queue()
        # 创建线程池对象
        self.pool = Pool()

    def get_url_list(self):
        for page in range(1,14):
            url = self.base_url.format(page)
            self.url_queue.put(url)

    def exec_task(self):
        print('exec_task')
        url = self.url_queue.get()
        response = requests.get(url,headers=self.headers)
        html = response.content.decode('utf-8')

        eroot = etree.HTML(html)
        contents = eroot.xpath('//div[@class="content"]')
        for content in contents:
            item = {}
            item["content"]=''.join(content.xpath('./span/text()'))
            print(item)
        self.url_queue.task_done()


    # 注意必须携带参数result
    # result 任务的执行结果
    def exec_task_finish(self,result):
        print('任务执行完成')
        self.pool.apply_async(self.exec_task,callback=self.exec_task_finish)

    def run(self):
        # 执行任务
        self.get_url_list()
        # callback 执行完成任务后回调
        for idx in range(5):
            self.pool.apply_async(self.exec_task,callback=self.exec_task_finish)

        # 退出条件
        self.url_queue.join()

if __name__ == '__main__':
    spider = QiubaiSpider()
    spider.run()