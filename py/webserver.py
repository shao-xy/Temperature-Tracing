import sys
import socket
from threading import Thread

from commondefs import WEBSERVER_LISTEN_PORT

class ServingThread(Thread):
    def __init__(self, checker, clientsockettuple):
        Thread.__init__(self)
        self.checker = checker
        self.clientsocket, self.addr = clientsockettuple

    def run(self):
        print(f'[REQ] received from {self.addr}')
        self.clientsocket.send(self.checker.get().encode('utf-8'))

class Server(Thread):
    def __init__(self, tracer_daemon):
        Thread.__init__(self)
        self._daemon = tracer_daemon
        self._thrdpool = []

    def run(self):
        print('Server thread launch!')
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((socket.gethostname(), WEBSERVER_LISTEN_PORT))
        serversocket.listen(5)
        while True:
            new_thrd = ServingThread(self._daemon.checker, serversocket.accept())
            new_thrd.start()
            self._thrdpool.append(new_thrd)
    
    def __del__(self):
        for thrd in self._thrdpool:
            thrd.join()
