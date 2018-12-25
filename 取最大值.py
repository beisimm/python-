def GetMax(*args):
    max = args[0]
    a = args
    for i in range(len(args)):
        if args[i] > max:
            max = args[i]

    return max


if __name__ == '__main__':
    print(GetMax(1, 4, 7, 2, 5, 8, 3, 6, 9, 99, 1))
