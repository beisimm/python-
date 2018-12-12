# def fib(n):
#     current = 0
#     num1, num2 = 0, 1
#     while current < n:
#         yield num1
#         num1, num2 = num2, num1 + num2
#         current += 1
# #
# F = fib(50)
# for i in F:
#     print(i)


# fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)

# def foo(x):
#     print("executing foo(%s)" % (x))
#
#
# class A(object):
#     def foo(self, x):
#         print("executing foo(%s,%s)" % (self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo(%s,%s)" % (cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % x)
#
#
# # a = A()
# # a.foo()
# # A.foo(1)
# A.class_foo(1)
# A.static_foo(1)

class A(object):
    bar = 1

    def foo(self):
        print('foo')

    @staticmethod
    def static_foo():
        print('static_foo')
        print(A.bar)

    @classmethod
    def class_foo(cls):
        print('class_foo')
        print(cls.bar)
        cls().foo()

A.static_foo()
A.class_foo()
