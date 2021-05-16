import abc


class Context(abc.ABC):
    def __init__(self):
        self.__state: IState

    def request(self):
        self.__state.handle(self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_data):
        print("當前狀態" + new_data.__class__.__name__)
        self.__state = new_data


class IState(abc.ABC):
    @abc.abstractmethod
    def handle(self, context: Context):
        pass


class StateOne(IState):
    def handle(self, context: Context):
        context.state = StateTwo()


class StateTwo(IState):
    def handle(self, context: Context):
        context.state = StateOne()


if __name__ == '__main__':
    context = Context()
    context.state = StateOne()

    context.request()
    context.request()
    context.request()
    context.request()
    context.request()



