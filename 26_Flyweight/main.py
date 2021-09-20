import abc


class IString(abc.ABC):
    def __init__(self, value):
        self.__value = value


class String(IString):
    def __init__(self, value):
        super(String, self).__init__(value)


class StringFactory:
    __temp = {}

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls, key):
        if cls.__temp.__contains__(key):
            return cls.__temp.get(key)
        else:
            cls.__temp[key] = String(key)
            return cls.__temp.get(key)


if __name__ == '__main__':
    print(StringFactory.get_instance("test1"))
    print(StringFactory.get_instance("test2"))
    print(StringFactory.get_instance("test1"))
