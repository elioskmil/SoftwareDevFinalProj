import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #Creates a blank white canvas window
        self.setWindowTitle("Massive Whiteboard")
        self.setGeometry(100, 100, 1080, 720)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

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
        ## TODO:

    def SansText(self):
        ### TODO: 

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

if __name__ == "__main__":

    MassiveWhiteBoard = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(MassiveWhiteBoard.exec())
