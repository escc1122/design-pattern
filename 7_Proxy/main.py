import abc


class IProxy(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def to_do(self, number_a, number_b) -> float:
        pass


class Add(IProxy):
    def __init__(self):
        super().__init__()

    def to_do(self, number_a, number_b) -> float:
        return number_a + number_b


class Sub(IProxy):
    def __init__(self):
        super().__init__()

    def to_do(self, number_a, number_b) -> float:
        return number_a - number_b


class Proxy(IProxy):
    def __init__(self, proxy: IProxy):
        self.__proxy = proxy

    def to_do(self, number_a, number_b) -> float:
        return self.__proxy.to_do(number_a, number_b)


if __name__ == '__main__':
    add = Proxy(Add())

    print(add.to_do(10, 5))  # 15

    sub = Proxy(Sub())

    print(sub.to_do(10, 5))  # 5
