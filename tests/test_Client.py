import pickle
from unittest import TestCase

from client.backend import Client

## first run the server from the cmd, then chack one by one the tests (dont run all the tests together)

class TestClient(TestCase):

    def test_connected(self):
        client = Client(ui=True)
        client.name = "user1"
        client._client = client.name
        client._connect_with_available_port("127.0.0.1", 50000)
        self.assertTrue(client.Connected)


    def test__connect_with_available_port(self):
        client = Client(ui=True)
        client.name = "user1"
        client._client = client.name
        self.assertTrue(client._connect_with_available_port("127.0.0.1",50000))

    def test_connect(self):
        client = Client(ui=True)
        client.name = "user1"
        client._client = client.name
        self.assertTrue(client.connect(client.name,"127.0.0.1",50000))

    def test_is_message(self):
        data = "MSG"
        client = Client(ui=True)
        client.name = "user1"
        client._client = client.name
        self.assertTrue(client.is_message(data))


