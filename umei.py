import requests
import re
import threading
from multiprocessing import Process

def down_picture(search, headers, Num):
    print("开始下载: ", Num)
    img_response = requests.get(url=search, headers=headers)

    with open("./umei/umei%d.jpg" % Num, "wb") as f:
        f.write(img_response.content)
    print("下载完成", Num)

for Num in range(2, 100):
    # print(Num)
    url = "http://www.umei.cc/meinvtupian/meinvmote/13393_%s.htm" % Num
    # url = "http://www.umei.cc/meinvtupian/meinvmote/13393_10.htm"
    # print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    content = response.content.decode('utf-8')
    # with open("umei.html", "w") as f:
    #     f.write(response.content.decode())
    # print(re.search("404 Not Found", content))
    # print(content)
    if re.search("404 Not Found", content):
        break

    # with open("umei%d.html" % Num, "wb") as f:
    #     f.write(response.content)

    search = re.findall(r'" src="(.*jpg) "', content)[0]
    # print(search)
    # down_picture(search, headers, Num)
    threading.Thread(target=down_picture, args=(search, headers, Num)).start()
