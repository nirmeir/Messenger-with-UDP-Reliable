from unittest import TestCase

import client
import clientapp
from client.backend import Client, OpCode
from server import serverapp


class TestHandler(TestCase):
    def setup (self):
        self._handlers = {
            OpCode.LST: self.handle_lst,
            OpCode.DL: self.handle_dl,
            OpCode.CM: self.handle_cm,
            OpCode.ACM: self.handle_acm,
            OpCode.CCN: self.handle_ccn,
            OpCode.MSG: self.handle_msg

        }

    def test_request_messages(self):
        client = clientapp
        server = serverapp

        server.send(OpCode.LST)
        resp = client.receive()
        self.assertEqual(resp)

    def test_handle_lst(self):
        self.fail()

    def test__init_udp_client(self):
        self.fail()

    def test__receive_over_udp(self):
        self.fail()

    def test_handle_dl(self):
        self.fail()

    def test_handle_cm(self):
        self.fail()

    def test_handle_acm(self):
        self.fail()

    def test_handle_ccn(self):
        self.fail()
