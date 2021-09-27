# https://ithelp.ithome.com.tw/articles/10200945
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p08_define_decorators_as_part_of_class.html


import types
from functools import wraps


class Init:
    def __init__(self, func):
        print("__init__")
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        print("__call__")
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        print("__get__")
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


def after_log(func):
    def a(self):
        func(self)
        print("after Log")

    return a


class BeforeLog:
    def operation(self, func):
        def a(*args):
            print("before Log")
            func(*args)

        return a


b = BeforeLog()


class AnyBusiness:
    @Init
    @after_log
    @b.operation
    def operation(self):
        print("business start")


if __name__ == '__main__':
    main_class = AnyBusiness()
    main_class.operation()
