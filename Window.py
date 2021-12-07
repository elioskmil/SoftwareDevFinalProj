import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from P2PNode import P2PNode

class Window(QMainWindow):
    def __init__(self, host='localhost', port=5000):
        super().__init__()
        #Initialises stored IP and port variables
        self.host = host
        self.port = port

        #Creates a blank white canvas window
        self.setWindowTitle("Massive Whiteboard")
        self.setGeometry(100, 100, 1080, 720)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        #Uses stored host and port variables to create a peer to peer node
        self.P2PNode = P2PNode(self.host, self.port, self)

        #Sets default drawing tool to a 4 pixel size black brush
        self.drawing = False
        self.bSize = 4
        self.bColor = Qt.black

        self.lastPoint = QPoint()

        #adds a toolbar menu for changing the size and color of the drawing tool
        #TODO: add icons, generally clean up GUI
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        bSize = mainMenu.addMenu("Size")
        bColor = mainMenu.addMenu("Color")
        textTool = mainMenu.addMenu("Text") #TODO: fully implement this feature
        connections = mainMenu.addMenu("Connections")

        smallBrush = QAction("Small", self)
        bSize.addAction(smallBrush)
        smallBrush.triggered.connect(self.SmallSize)

        medBrush = QAction("Medium", self)
        bSize.addAction(medBrush)
        medBrush.triggered.connect(self.MediumSize)

        largeBrush = QAction("Large", self)
        bSize.addAction(largeBrush)
        largeBrush.triggered.connect(self.LargeSize)

        TNRBoxer = QAction("Times New Roman", self)
        textTool.addAction(TNRBoxer)
        TNRBoxer.triggered.connect(self.TNRText)

        SansBoxer = QAction("Comic Sans", self)
        textTool.addAction(SansBoxer)
        SansBoxer.triggered.connect(self.SansText)

        black = QAction("Black", self)
        bColor.addAction(black)
        black.triggered.connect(self.blackB)

        white = QAction("White", self)
        bColor.addAction(white)
        white.triggered.connect(self.whiteB)

        red = QAction("Red", self)
        bColor.addAction(red)
        red.triggered.connect(self.redB)

        green = QAction("Green", self)
        bColor.addAction(green)
        green.triggered.connect(self.greenB)

        blue = QAction("Blue", self)
        bColor.addAction(blue)
        blue.triggered.connect(self.blueB)

        #TODO: add color wheel?

        manage = QAction("Manage Connections", self)
        connections.addAction(manage)
        manage.triggered.connect(self.manageConnections)

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):

        if(event.buttons() & Qt.LeftButton) & self.drawing:
            paintBrush = QPainter(self.image)
            paintBrush.setPen(QPen(self.bColor, self.bSize, Qt.SolidLine,
                                                Qt.RoundCap, Qt.RoundJoin))
            paintBrush.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPaint = QPainter(self)
        canvasPaint.drawImage(self.rect(), self.image, self.image.rect())

    def drawUpdate(self, event):
        """
        Updates the drawing based on what the other node sends. e.g. If one node
        user draws a line, that line will appear on the other program
        """
        paintBrush = QPainter(self.image)
        pen = QPen()
        # pen.setWidth(self.bSize) #FIXME: for some reason the program doesn't
                                   #FIXME: play nicely with width
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        try:
            if self.bColor == Qt.black:
                pen.setColor(Qt.black)
            elif self.bColor == Qt.white:
                pen.setColor(Qt.white)
            elif self.bColor == Qt.red:
                pen.setColor(Qt.red)
            elif self.bColor == Qt.green:
                pen.setColor(Qt.green)
            elif self.bColor == Qt.blue:
                pen.setColor(Qt.blue)
        except Exception as e:
            print(e)
        paintBrush.setPen(pen)
        paintBrush.drawLine(self.lastPoint, event.pos())
        self.lastPoint = event.pos()
        self.update()

    def makeJson(self):
        return json.dumps({'x': self.lastPoint.x(), 'y': self.lastPoint.y(),
                           'color': self.bColor, 'size': self.bSize})

    def jsonPaint(self, json_dict):
        local_point_x = self.lastPoint.x()
        local_point_y = self.lastPoint.y()
        local_color = self.bColor
        local_size = self.bSize
        self.lastPoint = QPoint(json_dict['x'], json_dict['y'])
        self.bColor = json_dict['color']
        #self.bSize = int(json_dict['size'])
        self.drawUpdate(QMouseEvent(
            QEvent.MouseButtonRelease,
            self.lastPoint,
            Qt.LeftButton,
            Qt.LeftButton,
            Qt.NoModifier))
        self.bColor = local_color
        self.bSize = local_size
        self.lastPoint = QPoint(local_point_x, local_point_y)

    def updateClient(self, json_dict=None):
        if json_dict:
            self.jsonPaint(json_dict)

    def updatePeers(self):
        self.P2PNode.send_to_nodes(self.makeJson())

    def save(self):
        #TODO: Autosave feature?
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                            "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filePath == "":
            return
        self.image.save(filePath)

    def SmallSize(self):
        self.bSize = 4

    def MediumSize(self):
        self.bSize = 7

    def LargeSize(self):
        self.bSize = 10

    def TNRText(self):
        raise NotImplementedError("ToDo")
        # TODO:


    def SansText(self):
        raise NotImplementedError("ToDo")
        # TODO:

    #TODO: textbox stuff goes here

    def blackB(self):
        self.bColor = Qt.black

    def whiteB(self):
        self.bColor = Qt.white

    def redB(self):
        self.bColor = Qt.red

    def greenB(self):
        self.bColor = Qt.green

    def blueB(self):
        self.bColor = Qt.blue

    def manageConnections(self):
        target, success = QInputDialog.getText(self, 'IP Address input Dialog',
                                               'Enter target (format: 192.168.0.1:5000)')
        ip, port = target.split(":")
        self.P2PNode.connect_with_node(ip, int(port))

def main():
    MassiveWhiteBoard = QApplication(sys.argv)
    host = 'localhost'
    port = 8000
    for arg_index in range(len(sys.argv)):
        if arg_index == 1:
            host = sys.argv[arg_index]
        if arg_index == 2:
            port = int(sys.argv[arg_index])
    window = Window(host, port)

    window.show()
    MassiveWhiteBoard.exec()

if __name__ == "__main__":
    main()
