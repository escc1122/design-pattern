import abc


class ICollection(abc.ABC):
    def __init__(self, array: []):
        self._list = array

    def get(self):
        pass


class List(ICollection):
    def get(self):
        return self._list


class MayBeOtherList(ICollection):
    def get(self):
        return self._list


class ICollections(abc.ABC):
    @classmethod
    def sort(cls, collection: ICollection):
        collection.get().sort()


if __name__ == '__main__':
    b = List([5, 3, 6, 8, 9, 10])
    maybe = MayBeOtherList([15, 3, 7, 8, 9, 10])
    print(b.get())
    ICollections.sort(b)
    print(b.get())
    print(maybe.get())
    ICollections.sort(maybe)
    print(maybe.get())
