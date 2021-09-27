class Facade:
    def __init__(self):
        self.__subClassOne = SubClassOne()
        self.__subClassTwo = SubClassTwo()

    def flow_a_to_d(self):
        self.__subClassOne.to_do_a()
        self.__subClassOne.to_do_b()
        self.__subClassTwo.to_do_c()
        self.__subClassTwo.to_do_d()


class SubClassOne:
    def to_do_a(self):
        print("SubClassOne to_do_a")

    def to_do_b(self):
        print("SubClassOne to_do_b")


class SubClassTwo:
    def to_do_c(self):
        print("SubClassTwo to_do_c")

    def to_do_d(self):
        print("SubClassTwo to_do_d")


if __name__ == '__main__':
    facade = Facade()
    facade.flow_a_to_d()
