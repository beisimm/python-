import gevent

def eat():
    while True:
        print("eat")
        gevent.sleep(1)

def speak():
    while True:
        print('speak')
        gevent.sleep(1)

def main():
    spand_chi = gevent.spawn(eat)
    spand_chi.join()

if __name__ == '__main__':
    main()
