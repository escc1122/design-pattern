import abc
import threading
import time
from multiprocessing import Process, Pool


# import multiprocessing


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
        # time.sleep(5)
        self._worker.action_a()


class CommandB(ICommand):
    def __init__(self, worker2: Worker):
        super().__init__(worker2)

    def execute(self):
        # time.sleep(3)
        self._worker.action_b()


class Invoker:
    _instance_lock = threading.Lock()

    def __init__(self):
        self.__command: [ICommand] = []

    def set_command(self, command: ICommand):
        self.__command.append(command)

    def execute_command(self):
        while len(self.__command) > 0:
            p = Process(target=self.__command.pop(0).execute)
            p.start()


def job1(worker, invoker):
    print("job1")
    invoker.set_command(CommandB(worker))
    invoker.set_command(CommandA(worker))
    # invoker.execute_command()
    # time.sleep(0.1)


def job2(invoker):
    print("job2")
    invoker.execute_command()


def test(worker, invoker):
    invoker.set_command(CommandB(worker))
    invoker.set_command(CommandA(worker))
    invoker.execute_command()


if __name__ == '__main__':
    worker = Worker()
    invoker = Invoker()
    # commandA = CommandA(worker)
    # invoker.set_command(commandA)
    # invoker.set_command(CommandB(worker))
    # job(worker, invoker)
    # time.sleep(4)
    # print("============add two===================")
    # pool = Pool(4)
    # for i in range(100):
    #     p = Process(target=job1, args=(worker, invoker))
    #     p.start()
    #
    # # for i in range(1000):
    # #     job2(invoker)
    # #
    # for i in range(100):
    #     p = Process(target=job2, args=(invoker,))
    #     p.start()
    #
    # invoker.execute_command()
    for i in range(100):
        p = Process(target=test, args=(worker, invoker))
        p.start()

    for i in range(10000):
        job2(invoker)
        # test()
