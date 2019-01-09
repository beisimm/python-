import stackless
import time

def call_wrapper(f, args, kwargs, result_ch):
    result_ch.send(f(*args, **kwargs))

def call(f, *args, **kwargs):
    result_ch= stackless.channel()
    stackless.tasklet(call_wrapper)(f, args, kwargs, result_ch)
    return result_ch.receive()
def factorial(n):
    if n <= 1:
        return 1
    return n * call(factorial, n-1)

st = time.time()

factorial(10000)
print (time.time() - st)
