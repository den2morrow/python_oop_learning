class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    __ip = 0

    def __init__(self):
        self.buffer = []
        self.ip = self.__ip + 1
        Server.__ip += 1
        self.to_send = []

    def send_data(self, data: Data):
        self.to_send.append(data)

    def get_data(self):
        temp_buffer = self.buffer
        self.buffer = []
        return temp_buffer

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = []

    def link(self, server: Server):
        self.servers.append(server)

    def unlink(self, server: Server):
        self.servers.remove(server)

    def send_data(self):
        for server in self.servers:
            if len(server.to_send) > 0:
                self.buffer.append(server.to_send.pop(0))

        while len(self.buffer) > 0:
            buf = self.buffer.pop(0)
            for server in self.servers:
                if server.get_ip() == buf.ip:
                    server.buffer.append(buf)
                    break


if __name__ == "__main__":
    router = Router()
    sv_from = Server()
    sv_from2 = Server()
    router.link(sv_from)
    router.link(sv_from2)
    router.link(Server())
    router.link(Server())
    sv_to = Server()
    router.link(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    sv_from2.send_data(Data("Hello", sv_to.get_ip()))
    sv_to.send_data(Data("Hi", sv_from.get_ip()))
    router.send_data()
    msg_lst_from = sv_from.get_data()
    msg_lst_to = sv_to.get_data()
