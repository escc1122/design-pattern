import abc
from abc import ABC


class IDecorator(abc.ABC):
    @abc.abstractmethod
    def operation(self):
        pass


class Log(IDecorator, ABC):
    def __init__(self):
        self._decorator: IDecorator = None


class AfterLog(Log):
    def set_component(self, decorator: IDecorator):
        self._decorator = decorator

    def operation(self):
        self._decorator.operation()
        print("after Log")


class BeforeLog(Log):
    def set_component(self, decorator: IDecorator):
        self._decorator = decorator

    def operation(self):
        print("before Log")
        self._decorator.operation()


class AnyBusiness(IDecorator):
    def operation(self):
        print("business start")


if __name__ == '__main__':
    main_class = AnyBusiness()
    beforeLog = BeforeLog()
    afterLog = AfterLog()

    afterLog.set_component(main_class)
    beforeLog.set_component(afterLog)

    beforeLog.operation()
