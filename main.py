import sys
from PyQt5.QtGui import QFont, QPixmap, QIcon, QMovie
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QBoxLayout, QVBoxLayout, QWidget,
                             QGroupBox, QLabel)

from fijoDistintoTamaño import MemoriaDistinta
from fijoMismoTamaño import MemoriaFija
from dinamicoMejorAjuste import MemoriaDinamica

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(300, 320)
        QMainWindow.setWindowFlags(self,Qt.MSWindowsFixedSizeDialogHint|Qt.WindowCloseButtonHint)#Desabilitar la bandera de maximizar
        self.setWindowIcon(QIcon("gravedad.png"))
        self.setWindowTitle("SIMULADOR")
        self.setStyleSheet("QGroupBox {background: rgba(0, 0, 0,1); border: blue;} QMainWindow{background-color:  rgba(0, 45, 60, 0.3)}")
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.windowFMT = MemoriaFija()
        self.windowDT = MemoriaDistinta()
        self.windowMD = MemoriaDinamica()

        self.group = QGroupBox(self.centralWidget)
        movie = QMovie("wave.gif")
        self.gifLabel = QLabel(self.group)
        self.gifLabel.setGeometry(QRect(-200,20,500,500))
        self.gifLabel.setMovie(movie)
        movie.start()

        font = QFont()
        font.setPointSize(10)
        self.btMF = QPushButton("PARTICION FIJA-MT",self.group)
        self.btMF.setGeometry(QRect(70,60,150,35))
        self.btMF.setFont(font)
        self.btMFD = QPushButton("PARTICION FIJA-DT",self.group)
        self.btMFD.setGeometry(QRect(70,110,150,35))
        self.btMFD.setFont(font)
        self.btMD = QPushButton("PARTICION DINAMICA",self.group)
        self.btMD.setGeometry(QRect(70,160,150,35))
        self.btMD.setFont(font)
        vl =QVBoxLayout()
        vl.addWidget(self.group)
        self.centralWidget.setLayout(vl)

        self.windowMD.btRegresar.clicked.connect(self.regresarInicio)
        self.windowDT.btRegresar.clicked.connect(self.regresarInicio)
        self.windowFMT.btRegresar.clicked.connect(self.regresarInicio)

        self.btMF.clicked.connect(self.showMF)
        self.btMFD.clicked.connect(self.showMFD)
        self.btMD.clicked.connect(self.showMD)

    def regresarInicio(self):
        self.windowDT.hide()
        self.windowMD.hide()
        self.windowFMT.hide()
        self.show()

    def showMF(self):
        self.hide()
        self.windowDT.hide()
        self.windowMD.hide()
        self.windowFMT.show()
    def showMFD(self):
        self.hide()
        self.windowMD.hide()
        self.windowFMT.hide()
        self.windowDT.show()
    def showMD(self):
        self.hide()
        self.windowDT.hide()
        self.windowFMT.hide()
        self.windowMD.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow= MainWindow()
    mainWindow.show()
    app.exec_()