import abc


class Facade(abc.ABC):
    class __SubClassOne(abc.ABC):
        @classmethod
        def to_do_a(cls):
            print("SubClassOne to_do_a")

        @classmethod
        def to_do_b(cls):
            print("SubClassOne to_do_b")

    class __SubClassTwo(abc.ABC):
        @classmethod
        def to_do_c(cls):
            print("SubClassTwo to_do_c")

        @classmethod
        def to_do_d(cls):
            print("SubClassTwo to_do_d")

    @classmethod
    def facade_a(cls):
        cls.__SubClassOne().to_do_a()
        cls.__SubClassTwo().to_do_c()

    @classmethod
    def facade_b(cls):
        cls.__SubClassOne().to_do_b()
        cls.__SubClassTwo().to_do_d()


if __name__ == '__main__':
    facade = Facade()
    # SubClassOne to_do_a
    # SubClassTwo to_do_c
    # == == == == == == == == == == == ==
    # SubClassOne to_do_b
    # SubClassTwo to_do_d
    facade.facade_a()
    print("========================")
    facade.facade_b()
