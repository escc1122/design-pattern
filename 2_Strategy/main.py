import abc


class IStrategy(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def to_do(self, number_a, number_b) -> float:
        pass


class Add(IStrategy):
    def __init__(self):
        super().__init__()

    def to_do(self, number_a, number_b) -> float:
        return number_a + number_b


class Sub(IStrategy):
    def __init__(self):
        super().__init__()

    def to_do(self, number_a, number_b) -> float:
        return number_a - number_b


class Strategy:
    def __init__(self, strategy: IStrategy):
        self.__strategy = strategy

    def do_it(self, number_a, number_b) -> float:
        return self.__strategy.to_do(number_a, number_b)


if __name__ == '__main__':
    add = Strategy(Add())

    print(add.do_it(10, 5))  # 15

    sub = Strategy(Sub())

    print(sub.do_it(10, 5))  # 5
