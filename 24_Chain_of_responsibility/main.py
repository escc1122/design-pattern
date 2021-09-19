import abc


class Request:
    def __init__(self):
        self.__type = None
        self.__msg = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, d):
        self.__type = d

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, d):
        self.__msg = d


class IHandler(abc.ABC):
    def __init__(self):
        self._next_handler: IHandler = None

    def set_next_handler(self, handler):
        self._next_handler: IHandler = handler

    def handler_request(self):
        pass


class Handler1(IHandler):
    def handler_request(self, request: Request):
        if request.type == 1:
            print("Handler1 : " + request.msg)
        elif self._next_handler is not None:
            self._next_handler.handler_request(request)
        else:
            print("Handler1 no next")


class Handler2(IHandler):
    def handler_request(self, request: Request):
        if request.type == 2:
            print("Handler2 : " + request.msg)
        elif self._next_handler is not None:
            self._next_handler.handler_request(request)
        else:
            print("Handler2 no next")


if __name__ == '__main__':
    r1 = Request()
    r1.type = 1
    r1.msg = "test r1"

    r2 = Request()
    r2.type = 2
    r2.msg = "test r2"

    h1 = Handler1()
    h2 = Handler2()
    h1.set_next_handler(h2)

    h1.handler_request(r1)
    h1.handler_request(r2)
