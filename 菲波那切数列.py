def fib_recur(n):
    '''
    斐波那契数列
    :param n: 整数
    :return:
    '''
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


def Fibonacci_Loop(n):
    result_list = []
    a, b = 0, 1
    while n > 0:
        result_list.append(b)
        a, b = b, a + b
        n -= 1
    return result_list


def fib_iterator(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a


class Fibonacci(object):
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        if self.num < 1:
            return 1
        a, b = 0, 1
        while self.num > 0:
            a, b = a + b, a
            self.num -= 1
            yield a

    def __next__(self):
        return self.__iter__()


def FibLoop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a, end=' ')

if __name__ == '__main__':
    FibLoop(10)
