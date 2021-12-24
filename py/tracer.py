from webserver import Server
from checker import Checker

class Tracer():
    def __init__(self):
        self.server = Server(self)
        self.checker = Checker()

    def launch(self):
        self.server.start()
        self.checker.start()
