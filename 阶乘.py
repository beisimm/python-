def FactorialRecursion(n):
    '''
    阶乘的递归实现
    :param n:正整数
    :return:阶乘结果
    '''
    if n == 1:
        return 1
    else:
        return n * FactorialRecursion(n - 1)


def Factorial_Iter(n):
    '''
    阶乘的迭代实现
    :param n: 正整数
    :return: 阶乘结果
    '''
    result = n
    for i in range(1, n):
        result *= i
    return result
