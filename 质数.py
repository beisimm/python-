import math


def PrimeNumber(num):
    '''判断是不是质数'''
    try:
        num = int(num)
    except:
        print("您输错了")  # 首先判断是否是一个数字, 这里用try来保证程序的健壮
    else:
        if num >= 2:  # 判断是否是大于1的整数, 如果不是没有任何意义
            if num == 2:
                print("这是一个质数")
            else:
                for s in range(2, math.ceil(num / 2) + 1):
                    if num % s == 0:
                        print("这不是一个质数, 他能被%d整除" % s)
                        break
                print("这是一个质数")
        else:
            print("请输入大于1的整数")


if __name__ == '__main__':
    PrimeNumber(97)
