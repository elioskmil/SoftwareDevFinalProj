import sys
import time
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from P2PNode import P2PNode

class testP2PNode:
    def test_p2pnode(self):
        picture = QImage(self.size(), QImage.Format_RGB32)
        node1 = P2PNode("localhost", 7777, picture)
        node2 = P2PNode("localhost", 8888, picture)

        time.sleep(1)

        node1.connect_with_node("localhost", 8888)
        if(node1.send_ping()):
            assert True
        assert False
