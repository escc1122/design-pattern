import abc


class IAggregate(abc.ABC):
    def __init__(self):
        self._list = []
        self._iterator

    @abc.abstractmethod
    def iterator(self):
        pass


class Books(IAggregate):
    def __init__(self):
        self._iterator = Iterator(self)

    def append(self, string: str):
        self._list.append(string)

    def size(self):
        return len(self._list)

    def iterator(self):
        return self._iterator


class IIterator(abc.ABC):
    def __init__(self, aggregate: IAggregate):
        self._aggregate = aggregate
        self._index = 0
        # self._i_trees: [IComposite] = []

    @abc.abstractmethod
    def next(self, i_tree):
        pass

    @abc.abstractmethod
    def has_next(self, i_tree):
        pass


class Iterator(IIterator):
    def __init__(self, aggregate: IAggregate):
        super().__init__(aggregate)

    def next(self):
        a = self._aggregate._list[self._index]
        self._index = self._index + 1

        return a

    def has_next(self) -> bool:
        r = False
        if self._aggregate.size() > self._index:
            r = True
        else:
            r = False
        return r


if __name__ == '__main__':
    books = Books()
    books.append("boob1")
    books.append("boob2")
    books.append("boob3")
    iterator = books.iterator()
    while iterator.has_next():
        print(iterator.next())
