from nuvole import Server, Service
from tornado.web import HTTPError
from urllib.error import HTTPError as urllibHTTPError
from threading import Thread
from urllib.request import Request, urlopen
from time import sleep
from random import randrange
import json
import logging


HOST = 'localhost'
PORT = 8080


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)16s - %(levelname)8s - %(message)s'
)
log = logging.getLogger('test')


class Context:

    def __init__(self):
        self.hello = 'Hello World'


class MyService(Service):

    PATH = r'/page/*'
    VERBOSE = True

    def get(self):
        self.write(self.context.hello)

    def post(self):
        number = self.body.get('random number')
        if number == 6:
            raise HTTPError(400, 'the die is cast')
        self.write(self.body)


class BadService(Service):

    PATH = r'/bad/*'

    def get(self):
        raise HTTPError(400, 'You are looking for a bad page')


class Tester(Thread):

    def run(self):
        url = f'http://{HOST}:{PORT}/page'
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json'
        }
        sleep(2)
        for i in range(5):
            die = randrange(1, 7)
            data = json.dumps({'random number': die}).encode('utf-8')
            request = Request(url, data=data, method='POST', headers=headers)
            try:
                urlopen(request)
            except urllibHTTPError:
                pass
            sleep(0.5)


if __name__ == '__main__':

    tester = Tester()
    tester.start()

    services = [MyService, BadService]
    context = Context()
    server = Server(services, context)
    server.run(HOST, PORT)
