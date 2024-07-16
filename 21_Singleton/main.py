import threading
import time
import threading


class Singleton:
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(2)

    @staticmethod
    def get_instance():
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton()
        return Singleton._instance


class Singleton2:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        # 初始化代码
        pass


class Test:
    def __init__(self):
        pass


def task(arg):
    obj = Singleton.get_instance()
    # obj = Singleton2()
    print(obj)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()

    # a = Singleton2()
    # b = Singleton2()
    # print(a)
    # print(b)
    # a = Test()
    # b = Test()
    # print(a)
    # print(b)
# <__main__.Singleton object at 0x00000245C7D70FA0>
# <__main__.Singleton object at 0x00000245C7D70FA0>
# <__main__.Singleton2 object at 0x00000245C7DC5640>
# <__main__.Singleton2 object at 0x00000245C7DC5640>
# <__main__.Test object at 0x00000245C7DC5D60>
# <__main__.Test object at 0x00000245C7DC5370>
