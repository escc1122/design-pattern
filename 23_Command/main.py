import abc


class Worker:
    def __init__(self):
        pass

    def action_a(self):
        print("to do action_a")

    def action_b(self):
        print("to do action_b")


class ICommand(abc.ABC):
    def __init__(self, worker5: Worker):
        self._worker = worker5

    def execute(self):
        pass


class CommandA(ICommand):
    def __init__(self, worker1: Worker):
        super().__init__(worker1)

    def execute(self):
        self._worker.action_a()


class CommandB(ICommand):
    def __init__(self, worker2: Worker):
        super().__init__(worker2)

    def execute(self):
        self._worker.action_b()


class Invoker:
    def __init__(self):
        self.__command: [ICommand] = []

    def set_command(self, command: ICommand):
        self.__command.append(command)

    def execute_command(self):
        while len(self.__command) > 0:
            self.__command.pop(0).execute()


if __name__ == '__main__':
    worker = Worker()
    print(worker)
    invoker = Invoker()
    commandA = CommandA(worker)
    invoker.set_command(commandA)
    invoker.set_command(CommandB(worker))

    invoker.execute_command()
