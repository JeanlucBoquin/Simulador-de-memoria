import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow, QPushButton, QLabel, QGroupBox,
                            QVBoxLayout, QHBoxLayout,QTableWidget, QTableWidgetItem,
                            QAbstractItemView, QGridLayout, QComboBox, QFrame, QLineEdit
                            )

class MemoriaFija(QMainWindow):
    def __init__(self,sql=None):
        QMainWindow.__init__(self)
        QMainWindow.setWindowFlags(self,Qt.MSWindowsFixedSizeDialogHint)
        self.resize(400,350)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # self.label = QLabel(self)
        # self.label.setGeometry(QRect(0, 0, 540, 350))
        # # self.label.setPixmap(self.pixmap)
        # self.label.setScaledContents(True)

       # self.showTable()
        self.groupMainWindow()

    def groupMainWindow(self):
        self.groupControl = QGroupBox()

        self.etiqueta1 = QLabel("FIJO DISTINTO TAMAÑO")

        # h1 = QHBoxLayout()
        # h1.addWidget(self.etiqueta2)
        # h1.addWidget(self.seleccionarDivisionDeMemoria)

        self.etiqueta3 = QLabel("Nombre")
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText("Nombre del proceso")
        h2 = QHBoxLayout()
        h2.addWidget(self.etiqueta3)
        h2.addWidget(self.lineEdit1)

        self.etiqueta4 = QLabel("Tamaño")
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("Cantidad de espacio en MB")
        h3 = QHBoxLayout()
        h3.addWidget(self.etiqueta4)
        h3.addWidget(self.lineEdit2)

        self.ptCargar = QPushButton("Cargar")
        self.ptLiberar = QPushButton("Liberar")
        h4 = QHBoxLayout()
        h4.addWidget(self.ptCargar)
        h4.addWidget(self.ptLiberar)

        v1 = QVBoxLayout()
        v1.addWidget(self.etiqueta1)
        # v1.addLayout(h1)
        v1.addLayout(h2)
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addSpacing(200)
        self.groupControl.setLayout(v1)


        self.groupSimulator = QGroupBox()
        self.line=QFrame()            #marco hereda el espacio del QMainWindow
        # self.line.setGeometry(QRect(215,20,2,510))      #posicion y tamañp
        self.line.setFrameShape(QFrame.VLine)           #forma linea en este caso
        self.line.setFrameShadow(QFrame.Raised)         #sombra
        # self.line.setLineWiddth(2)                       #grosor



        self.tablaBitacora = QTableWidget()
        self.tablaBitacora.setColumnCount(1)    #Establecer numero de columna
        self.tablaBitacora.setRowCount(2)       #Establecer numero de fila
        self.tablaBitacora.setMaximumWidth(100) #Establecer ancho maximo

        self.tablaBitacora.setItem(0, 0, QTableWidgetItem("8 MB"))
        self.tablaBitacora.item(0,0).setBackground(Qt.red)
        self.tablaBitacora.item(0,0).setTextAlignment(Qt.AlignCenter)

        nombrecolumnas=("RAM",)
        self.tablaBitacora.setHorizontalHeaderLabels(nombrecolumnas)#nombre de columna

        self.tablaBitacora.setAutoScroll(True)
        self.tablaBitacora.setAlternatingRowColors(True)
        self.tablaBitacora.verticalHeader().setDefaultSectionSize(20)       #alturas celda
        self.tablaBitacora.setColumnWidth(0,100)                            #anchura celda
        self.tablaBitacora.setRowHeight(0,10)
        self.tablaBitacora.setRowHeight(1,50)
        self.tablaBitacora.setRowHeight(2,90)

      
        """
            for indice, ancho in enumerate((anchura1,anchura2,anchura3),start=0):
                self.tablaBitacora.setColumnWidth(indice,ancho)
        """

        self.tablaBitacora.setEditTriggers(QAbstractItemView.NoEditTriggers)#Desabilitar editar celdas
        # self.tablaBitacora.setSelectionMode(QAbstractItemView.SingleSelection)#Seleccionar una celda a la vez
        # self.tablaBitacora.setSelectionMode(QAbstractItemView.NoSelection)#Desabilita la selecion
        self.tablaBitacora.setDragDropOverwriteMode(False)
        self.tablaBitacora.setSortingEnabled(False)#desabilita el ordenamiento
        self.tablaBitacora.verticalHeader().setVisible(False)#ocultar header verticales

        v2  = QVBoxLayout()
        v2.addWidget(self.tablaBitacora)
        self.groupSimulator.setLayout(v2)

        self.grid = QGridLayout()
        self.grid.addWidget(self.groupControl,0,0,1,1)
        self.grid.addWidget(self.line,0,1,2,1)
        self.grid.addWidget(self.groupSimulator,0,2,1,4)

        self.centralwidget.setLayout(self.grid)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MemoriaFija()
    main.show()
    app.exec_()