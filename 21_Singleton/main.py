class Singleton:
    _instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance


class Singleton2:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Test:
    def __init__(self):
        pass


if __name__ == '__main__':
    a = Singleton.get_instance()
    b = Singleton.get_instance()
    print(a)
    print(b)
    a = Singleton2()
    b = Singleton2()
    print(a)
    print(b)
    a = Test()
    b = Test()
    print(a)
    print(b)
# <__main__.Singleton object at 0x00000245C7D70FA0>
# <__main__.Singleton object at 0x00000245C7D70FA0>
# <__main__.Singleton2 object at 0x00000245C7DC5640>
# <__main__.Singleton2 object at 0x00000245C7DC5640>
# <__main__.Test object at 0x00000245C7DC5D60>
# <__main__.Test object at 0x00000245C7DC5370>
