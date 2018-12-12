import requests
from lxml import etree


class neihanSpider():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

    def get_url(self):
        url_list = []
        url_list.append("https://www.neihanba.com/dz/index.html")
        for Num in range(2, 1142):
            url_list.append("https://www.neihanba.com/dz/list_%d.html" % Num)
        return url_list

    def save_item(self, item):
        print(item)

    def run(self):
        url_list = self.get_url()
        for url in url_list:
            response = requests.get(url, headers=self.headers)
            list_html = response.content.decode("gbk")
            eroot = etree.HTML(list_html)
            li_elements_list = eroot.xpath('//li/h4/a/@href')  # 提取详情url
            for element in li_elements_list:
                url = "https://www.neihanba.com" + element
                response_detail = requests.get(url, headers=self.headers)
                detail_html = response_detail.content.decode("gbk")
                eroot = etree.HTML(detail_html)
                title = eroot.xpath('//h1/text()')  # 提取详情页标题
                content = eroot.xpath('//td/p/text()')  # 提取详情页内容
                item = {}
                item['title'] = title
                item['content'] = content
                self.save_item(item)


if __name__ == '__main__':
    neihan = neihanSpider()
    neihan.run()
