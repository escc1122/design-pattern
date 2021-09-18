import abc


class ISoft(abc.ABC):
    def run(self):
        pass


class SoftA(ISoft):
    def run(self):
        print("SoftA start")


class SoftB(ISoft):
    def run(self):
        print("SoftB start")


class IMobile(abc.ABC):
    def __init__(self):
        self._money: {str, ISoft} = {}

    def setup(self, key, soft: ISoft):
        pass

    def run(self, key):
        pass


class MobileA(IMobile):
    def setup(self, key, soft: ISoft):
        self._money[key] = soft

    def run(self, key):
        self._money[key].run()


if __name__ == '__main__':
    a = MobileA()
    a.setup("a", SoftA())
    a.setup("b", SoftB())

    a.run("a")
    a.run("b")
