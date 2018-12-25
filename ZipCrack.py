import zipfile
import time
import threading

startTime = time.time()
# 判断线程是否需要终止
flag = True


def extract(password, file):
    try:
        password = str(password)
        file.extractall(path='.', pwd=password.encode('utf-8'))
        print("the password is {}".format(password))
        nowTime = time.time()
        print("spend time is {}".format(nowTime - startTime))
        global flag
        # 成功解压其余线程终止
        flag = False
    except:
        pass


def do_main(start, end):
    start = int(start)
    end = int(end)
    zfile = zipfile.ZipFile("test.zip", 'r')
    # 开始尝试
    for number in range(start, end):
        print("Now password is:", number)
        if flag is True:
            extract(number, zfile)
            # t = threading.Thread(target=extract, args=(number, zfile))
            # t.start()
            # t.join()


if __name__ == '__main__':
    do_main(0, 99999999)
    # for i in range(10):
    #     threading.Thread(target=do_main, args=(i,)).start()
