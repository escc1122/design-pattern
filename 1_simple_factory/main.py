import abc


class ISimpleFactory(abc.ABC):
    def __init__(self):
        self.__numberA: float
        self.__numberB: float

    @abc.abstractmethod
    def to_do(self):
        pass

    @property
    def numberA(self):
        return self.__numberA

    @numberA.setter
    def numberA(self, new_data):
        self.__numberA = new_data

    @property
    def numberB(self):
        return self.__numberB

    @numberB.setter
    def numberB(self, new_data):
        self.__numberB = new_data


class Add(ISimpleFactory):
    def __init__(self):
        super().__init__()

    def to_do(self) -> float:
        return self.numberA + self.numberB


class Sub(ISimpleFactory):
    def __init__(self):
        super().__init__()

    def to_do(self) -> float:
        return self.numberA - self.numberB


class SimpleFactory:
    @staticmethod
    def create(factory_type) -> ISimpleFactory:
        if factory_type == 'add':
            return Add()
        elif factory_type == 'sub':
            return Sub()


if __name__ == '__main__':
    simpleFactory = SimpleFactory()
    add = simpleFactory.create("add")
    add.numberA = 10
    add.numberB = 5
    print(add.to_do())  # 15

    sub = simpleFactory.create("sub")
    sub.numberA = 10
    sub.numberB = 5
    print(sub.to_do())  # 5
