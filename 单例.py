class single_instance(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


if __name__ == '__main__':
    a = single_instance()
    b = single_instance()
    print(a)
    print(b)
