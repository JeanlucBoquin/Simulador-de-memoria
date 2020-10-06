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

        #Eventos 
        # self.btBitacora.clicked.connect(self.showBitacora)
        # # self.btMonitore.clicked.connect(self.showMonitoreo)
        # self.windowBitacora.btRegresar.clicked.connect(self.regresar)
        # self.windowMonitoreo.btRegresar.clicked.connect(self.regresar)
        self.btMF.clicked.connect(self.showMF)
        self.btMFD.clicked.connect(self.showMFD)
        self.btMD.clicked.connect(self.showMD)
            
    def showMF(self):
        self.hide()
        self.windowDT.hide()
        self.windowMD.hide()
        self.windowFMT.show()
    def showMFD(self):
        self.hide()
        self.windowDT.show()
        self.windowMD.hide()
        self.windowFMT.hide()
    def showMD(self):
        self.hide()
        self.windowDT.hide()
        self.windowMD.show()
        self.windowFMT.hide()
    # def regresar(self):
    #     self.show()
    #     self.windowBitacora.hide()
    #     self.windowMonitoreo.hide()
    # def showBitacora(self):
    #     self.hide()
    #     self.windowBitacora.establecerDatos()
    #     self.windowBitacora.show()
    # def showMonitoreo(self):
    #     self.hide()
    #     self.windowMonitoreo.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow= MainWindow()
    mainWindow.show()
    app.exec_()