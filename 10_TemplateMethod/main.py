import abc


class ITemplateMethod(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def condition(self) -> bool:
        pass

    @abc.abstractmethod
    def action(self):
        pass

    def flow(self):
        if self.condition():
            self.action()


class Crontab(ITemplateMethod):
    def __init__(self):
        super().__init__()

    def condition(self) -> bool:
        return True

    def action(self):
        print("Crontab is start")


if __name__ == '__main__':
    crontab1: ITemplateMethod = Crontab()
    # print Crontab is start
    crontab1.flow()
