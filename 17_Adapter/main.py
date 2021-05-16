import abc


class IAdapter(abc.ABC):
    @abc.abstractmethod
    def action_a(self):
        pass

    @abc.abstractmethod
    def action_b(self):
        pass


class PlayerOne(IAdapter):
    def action_a(self):
        print("PlayerOne action_a")

    def action_b(self):
        print("PlayerOne action_b")


class PlayerTwo(IAdapter):
    def action_a(self):
        print("PlayerTwo action_a")

    def action_b(self):
        print("PlayerTwo action_b")


class Adapter(IAdapter):
    def __init__(self):
        self.__other_player = OtherPlayer()

    def action_a(self):
        self.__other_player.action_aaaa()

    def action_b(self):
        self.__other_player.action_bbbb()


class OtherPlayer:
    def action_aaaa(self):
        print("OtherPlayer action_aaaa")

    def action_bbbb(self):
        print("OtherPlayer action_aaaa")


if __name__ == '__main__':
    player_one: IAdapter = PlayerOne()
    player_one.action_a()
    player_one.action_b()
    print("==========================")
    player_two: IAdapter = PlayerTwo()
    player_two.action_a()
    player_two.action_b()
    print("==========================")
    adapter: IAdapter = Adapter()
    adapter.action_a()
    adapter.action_b()



