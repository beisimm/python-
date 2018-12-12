import requests


class TiebaSpider():
    def __init__(self, kw, max_pn=1000):
        self.base_url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        self.kw = kw
        self.max_pn = max_pn

    def get_url_list(self):
        return [self.base_url.format(self.kw, pn) for pn in range(0, self.max_pn, 50)]

    def save_html(self, content, idx):
        with open('tieba_{}.html'.format(idx), 'wb') as f:
            f.write(content)

    def run(self):
        url_list = self.get_url_list()

        for url in url_list:
            response = requests.get(url, headers=self.headers)

            self.save_html(response.content, url_list.index(url))


if __name__ == '__main__':
    spider = TiebaSpider('显卡吧', 100)
    spider.run()