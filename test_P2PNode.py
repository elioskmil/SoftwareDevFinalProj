import sys
import time
import json
import unittest
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from P2PNode import P2PNode

class testP2PNode(unittest.TestCase):
    def setUp(self):
        pass

    def test_connections(self):
        picture = QImage()
        node1 = P2PNode("localhost", 7777, picture)
        node2 = P2PNode("localhost", 8888, picture)
        #node1.start()
        #node2.start()

        time.sleep(1)
        #assert node1.connect_with_node("localhost", 8888)
        if(node1.connect_with_node("localhost", 8888)):
            node1.stop()
            node2.stop()
            assert True
        node1.stop()
        node2.stop()
        assert False
    def test_disconnections(self):
        picture = QImage()
        node1 = P2PNode("localhost", 7777, picture)
        node2 = P2PNode("localhost", 8888, picture)
        #node1.start()
        #node2.start()

        time.sleep(1)

        node1.connect_with_node("localhost", 8888)
        time.sleep(1)

        if(node1.disconnect_with_node(node2)):
            node1.stop()
            node2.stop()
            assert True
        node1.stop()
        node2.stop()
        assert False

if __name__ == '__main__':
    unittest.main()