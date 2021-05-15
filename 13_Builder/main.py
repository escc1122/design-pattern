import abc


class Product(abc.ABC):
    def __init__(self):
        self.__teams = []

    def add(self, team):
        self.__teams.append(team)

    def show(self):
        for a in self.__teams:
            print(a)


class IBuild(abc.ABC):
    @abc.abstractmethod
    def build_a(self):
        pass

    @abc.abstractmethod
    def build_b(self):
        pass

    @abc.abstractmethod
    def get(self):
        pass


class BuildOne(IBuild):
    def __init__(self):
        self.__product = Product()

    def build_a(self):
        self.__product.add("build_a")

    def build_b(self):
        self.__product.add("build_b")

    def get(self):
        return self.__product


class BuildTwo(IBuild):
    def __init__(self):
        self.__product = Product()

    def build_a(self):
        self.__product.add("build_c")

    def build_b(self):
        self.__product.add("build_d")

    def get(self):
        return self.__product


class Director:
    def __init__(self):
        pass

    def construct(self, build: IBuild):
        build.build_a()
        build.build_b()


if __name__ == '__main__':
    # build_a
    # build_b
    # == == == == == == == == == ==
    # build_c
    # build_d
    director = Director()
    build_one = BuildOne()
    director.construct(build_one)
    build_one.get().show()
    print("====================")
    build_two = BuildTwo()
    director.construct(build_two)
    build_two.get().show()
