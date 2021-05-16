import abc


class IObserver(abc.ABC):
    @abc.abstractmethod
    def update(self, message):
        pass


class ObserverA(IObserver):
    def update(self, message):
        print("ObserverA to update message %s" % message)


class ObserverB(IObserver):
    def update(self, message):
        print("ObserverB to update message %s" % message)


class ISubject(abc.ABC):
    @abc.abstractmethod
    def attach(self, i_observer: IObserver):
        pass

    @abc.abstractmethod
    def detach(self, i_observer: IObserver):
        pass

    @abc.abstractmethod
    def notify(self, message: str):
        pass


class Subject(ISubject):
    def __init__(self):
        self.__observers: [IObserver] = []

    def attach(self, i_observer: IObserver):
        self.__observers.append(i_observer)

    def detach(self, i_observer: IObserver):
        self.__observers.remove(i_observer)

    def notify(self, message: str):
        for observer in self.__observers:
            observer.update(message)


if __name__ == '__main__':
    subject: ISubject = Subject()
    observer_a: IObserver = ObserverA()
    observer_b: IObserver = ObserverB()
    subject.attach(observer_a)
    subject.attach(observer_b)
    # ObserverA to update message al_test
    # ObserverB to update message al_test
    subject.notify("al_test")

    subject.detach(observer_b)
    # ObserverA to update message al_test2
    subject.notify("al_test2")
