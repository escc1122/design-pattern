import abc


class IComposite(abc.ABC):
    def __init__(self, name: str):
        self._name = name
        self._i_trees: [IComposite] = []

    @abc.abstractmethod
    def add(self, i_tree):
        pass

    @abc.abstractmethod
    def remove(self, i_tree):
        pass

    def show(self, depth=1):
        print(" " * depth + "--" + self._name)
        for tree in self._i_trees:
            tree.show(depth + 2)


class File(IComposite):
    def __init__(self, name: str):
        super().__init__(name)

    def add(self, i_tree: IComposite):
        print("file no add")

    def remove(self, i_tree: IComposite):
        pass

    # def show(self, depth=1):
    #     print("-" * depth + self.name)


class Folder(IComposite):
    def __init__(self, name: str):
        super().__init__(name)

    def add(self, i_tree: IComposite):
        self._i_trees.append(i_tree)

    def remove(self, i_tree: IComposite):
        self._i_trees.remove(i_tree)


if __name__ == '__main__':
    root: IComposite = Folder("root")
    folder_a = Folder("folder_a")
    folder_d = Folder("folder_d")
    folder_b = Folder("folder_b")
    folder_c = Folder("folder_c")
    folder_e = Folder("folder_e")
    folder_f = Folder("folder_f")
    file_a = File("file_a")
    file_d = File("file_d")
    file_b = File("file_b")
    file_c = File("file_c")
    file_e = File("file_e")
    file_f = File("file_f")

    root.add(folder_a)
    root.add(folder_d)
    root.add(file_a)
    root.add(file_d)
    root.add(file_b)
    folder_d.add(folder_b)
    folder_b.add(folder_e)
    folder_b.add(file_b)
    folder_b.add(file_c)
    folder_d.add(file_e)
    folder_e.add(folder_f)
    folder_f.add(file_f)

    root.show()
