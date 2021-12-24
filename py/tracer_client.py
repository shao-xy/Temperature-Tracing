import socket

from commondefs import WEBSERVER_LISTEN_PORT

class TracerClient():
    def __init__(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get(self):
        status = '(Server not running)'
        try:
            self._s.connect((socket.gethostname(), WEBSERVER_LISTEN_PORT))
            status = self._s.recv(4096).decode('utf-8')
            self._s.close()
        except ConnectionRefusedError:
            pass
        self.__init__()
        return status
