import abc


class IPrototype(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def clone(self):
        pass


class JustObject(IPrototype):
    def __init__(self):
        self.__number_a: float
        self.__number_b: float

    def clone(self):
        clone_object: JustObject = JustObject()
        clone_object.__number_a = self.__number_a
        clone_object.__number_b = self.__number_b
        return clone_object

    @property
    def number_a(self):
        return self.__number_a

    @number_a.setter
    def number_a(self, new_data):
        self.__number_a = new_data

    @property
    def number_b(self):
        return self.__number_b

    @number_b.setter
    def number_b(self, new_data):
        self.__number_b = new_data


if __name__ == '__main__':
    just_object = JustObject()
    just_object.number_a = 10
    just_object.number_b = 5
    # just_object number_a : 10 , number_b 5
    print("just_object number_a : %s , number_b %s" % (just_object.number_a, just_object.number_b))

    # clone_just_object number_a : 10 , number_b 5
    clone_just_object = just_object.clone()
    print("clone_just_object number_a : %s , number_b %s" % (clone_just_object.number_a, clone_just_object.number_b))
