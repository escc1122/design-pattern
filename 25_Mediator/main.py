import abc


class IColleague(abc.ABC):
    def __init__(self):
        self._mediator: IMediator = None

    def set_lunch_mediator(self, lunch_mediator):
        self._mediator = lunch_mediator

    def send(self, msg):
        self._mediator.send(msg, self)

    def notify(self, msg):
        print(self.__class__.__name__ + " : 不知道")


class ColleagueA(IColleague):
    def __init__(self):
        pass

    def notify(self, msg):
        print(self.__class__.__name__ + " : 隨便")


class ColleagueB(IColleague):
    def __init__(self):
        pass

    def notify(self, msg):
        print(self.__class__.__name__ + " : 不知道")


class IMediator(abc.ABC):
    def __init__(self):
        pass

    def send(self, msg, colleague: IColleague):
        pass


class LunchMediator(IMediator):
    def __init__(self):
        self.colleagueA: ColleagueA = None
        self.colleagueB: ColleagueB = None

    def send(self, msg, colleague: IColleague):
        print(colleague.__class__.__name__ + " : " + msg)
        if type(colleague) == ColleagueA:
            self.colleagueB.notify(msg)
        else:
            self.colleagueA.notify(msg)


if __name__ == '__main__':
    cA = ColleagueA()
    cB = ColleagueB()
    m = LunchMediator()

    cA.set_lunch_mediator(m)
    cB.set_lunch_mediator(m)

    m.colleagueA = cA
    m.colleagueB = cB

    cA.send("午餐吃什麼??")
    cB.send("午餐吃什麼??")
