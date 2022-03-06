from unittest import TestCase

from client.backend import Client, OpCode

# this tests check the server response while the client send commands
# first run the server from the cmd, then chack one by one the tests (dont run all the tests together)

class TestHandler(TestCase):

        def test_handle_lst(self):
            client = Client(ui=True)
            client.name = "user1"
            client._client = client.name
            client.connect(client.name, "127.0.0.1", 50000)
            client.send(OpCode.LST)
            self.assertTrue(client.receive())


        def test_handle_dl(self):
            client = Client(ui=True)
            client.name = "user1"
            client._client = client.name
            client.connect(client.name, "127.0.0.1", 50000)
            client.send(OpCode.DL)
            self.assertTrue(client.receive())


        def test_handle_cm(self):
            client = Client(ui=True)
            client.name = "user1"
            client._client = client.name
            client.connect(client.name, "127.0.0.1", 50000)
            client.send(OpCode.CM)
            resp = client.receive()
            self.assertTrue(resp == OpCode.SI)


        def test_handle_acm(self):
            client = Client(ui=True)
            client.name = "user1"
            client._client = client.name
            client.connect(client.name, "127.0.0.1", 50000)
            client.send(OpCode.ACM)
            resp = client.receive()
            self.assertTrue(resp == OpCode.SI)





