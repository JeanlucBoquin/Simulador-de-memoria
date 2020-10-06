import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow, QPushButton, QLabel, QGroupBox,
                            QVBoxLayout, QHBoxLayout,QTableWidget, QTableWidgetItem,
                            QAbstractItemView, QGridLayout, QComboBox, QFrame, QLineEdit
                            )

from Lista import Lista

class MemoriaDinamica(QMainWindow):
    def __init__(self,sql=None):
        QMainWindow.__init__(self)
        QMainWindow.setWindowFlags(self,Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowIcon(QIcon("ram.png"))
        self.setWindowTitle("Simulador de memoria")
        self.resize(400,350)
        self.lista = Lista()
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setStyleSheet("QGroupBox {background:rgba(245, 246, 250,.95)}")

        pixmap = QPixmap("fondoMain1.png")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 400, 370))
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        self.groupMainWindow()
        self.ptCargar.clicked.connect(self.agregarProceso)
        self.ptLiberar.clicked.connect(self.liberarProceso)
        # self.seleccionarDivisionDeMemoria.currentIndexChanged.connect(self.prueba)
        self.seleccionarDivisionDeMemoria.currentTextChanged.connect(self.prueba)
        self.seleccionarDivisionDeMemoriaLC.currentTextChanged.connect(self.prueba2)

    def prueba2(self):
        if self.seleccionarDivisionDeMemoriaLC.currentText() == "Cargar proceso":
            self.ptLiberar.setEnabled(False)
            self.ptCargar.setEnabled(True)
            self.lineEdit1.setEnabled(True)
            self.lineEdit2.setEnabled(True)

        elif self.seleccionarDivisionDeMemoriaLC.currentText() == "Liberar proceso":
            self.ptLiberar.setEnabled(True)
            self.ptCargar.setEnabled(False)
            self.lineEdit1.setEnabled(True)
            self.lineEdit2.setEnabled(False)

    def prueba(self):
        print(self.seleccionarDivisionDeMemoria.currentText())
        self.etiqueta1.setText("DINAMICO %s"%self.seleccionarDivisionDeMemoria.currentText())
        self.lista = Lista()
        self.tablaBitacora.setRowCount(0)

    def agregarProceso(self):
        nombre = self.lineEdit1.text()
        try:
            tamanio = int(self.lineEdit2.text())
        except Exception as e:
            print("campo vacio")
            tamanio = ""
        if nombre != "" and tamanio != "":
            bandera = self.lista.buscar(nombre)

            if self.seleccionarDivisionDeMemoria.currentText() == "MEJOR AJUSTE":
                self.lista.cargarProceso_PartDinamico_MejorAjuste(nombre,tamanio)
            elif self.seleccionarDivisionDeMemoria.currentText() == "PRIMER AJUSTE":
                self.lista.cargarProceso_PartDinamico_PrimerAjuste(nombre,tamanio)
            elif self.seleccionarDivisionDeMemoria.currentText() == "SIGUIENTE AJUSTE":
                self.lista.cargarProceso_PartDinamico_SiguienteAjuste(nombre,tamanio)

            self.lista.reEnumerarFila()
            nodo = self.lista.buscar(nombre)
            if self.tablaBitacora.rowCount()==8:
                self.tablaBitacora.setColumnWidth(0,100)
            try:
                if self.lista.memoriaDisponoble >= tamanio and bandera == False:
                    self.lista.reconstruirTabla(self.tablaBitacora)
                self.lista.listar()
            except Exception as e:
                print("Error desde ventada %s"%e)


    def liberarProceso(self):
        nombre = self.lineEdit1.text()
        if nombre != "":
            nodo = self.lista.buscar(nombre)
            self.lista.liberarProceso_PartDinamico(nombre)
            self.lista.reEnumerarFila()
            self.lista.reconstruirTabla(self.tablaBitacora)
            self.lista.listar()

 
    def groupMainWindow(self):
        self.groupControl = QGroupBox()



        self.etiqueta2 = QLabel("Metodo")
        self.seleccionarDivisionDeMemoria = QComboBox()
        self.seleccionarDivisionDeMemoria.addItem("MEJOR AJUSTE")
        self.seleccionarDivisionDeMemoria.addItem("PRIMER AJUSTE")
        self.seleccionarDivisionDeMemoria.addItem("SIGUIENTE AJUSTE")
        
        self.etiqueta22 = QLabel("Cargar/Liberar")
        self.seleccionarDivisionDeMemoriaLC = QComboBox()
        # self.seleccionarDivisionDeMemoriaLC.addItem("")
        self.seleccionarDivisionDeMemoriaLC.addItem("Cargar proceso")
        self.seleccionarDivisionDeMemoriaLC.addItem("Liberar proceso")

        h11 = QHBoxLayout()
        h11.addWidget(self.etiqueta22)
        h11.addWidget(self.seleccionarDivisionDeMemoriaLC)




        print(self.seleccionarDivisionDeMemoria.currentText())
        h1 = QHBoxLayout()
        h1.addWidget(self.etiqueta2)
        h1.addWidget(self.seleccionarDivisionDeMemoria)

        self.etiqueta1 = QLabel("DINAMICO MEJOR AJUSTE")

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
        self.ptLiberar.setEnabled(False)
        h4 = QHBoxLayout()
        h4.addWidget(self.ptCargar)
        h4.addWidget(self.ptLiberar)

        v1 = QVBoxLayout()
        v1.addWidget(self.etiqueta1)
        v1.addLayout(h1)
        v1.addLayout(h11)
        v1.addLayout(h2)
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addSpacing(170)
        self.groupControl.setLayout(v1)

        self.groupSimulator = QGroupBox()
        self.line=QFrame()            #marco hereda el espacio del QMainWindow
        self.line.setFrameShape(QFrame.VLine)           #forma linea en este caso
        self.line.setFrameShadow(QFrame.Raised)         #sombra

        self.tablaBitacora = QTableWidget()
        self.tablaBitacora.setColumnCount(1)    #Establecer numero de columna
        self.tablaBitacora.setMaximumWidth(100) #Establecer ancho maximo

        self.label = QLabel(self.groupControl)
        self.label.setGeometry(QRect(0,260,280,80))
        pix = QPixmap("blue.png")
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)
        # gif.start()
        # self.tablaBitacora.setItem(0, 0, QTableWidgetItem("8 MB"))
        # self.tablaBitacora.item(0,0).setBackground(Qt.red)
        self.btRegresar = QPushButton("Regresar",self.groupControl)
        self.btRegresar.setGeometry(QRect(5,310,90,25))

        nombrecolumnas=("RAM 56M",)
        self.tablaBitacora.setHorizontalHeaderLabels(nombrecolumnas)#nombre de columna

        self.tablaBitacora.setAutoScroll(True)
        self.tablaBitacora.setAlternatingRowColors(True)
        self.tablaBitacora.verticalHeader().setDefaultSectionSize(20)       #alturas celda
        self.tablaBitacora.setColumnWidth(0,100)                            #anchura celda
        self.tablaBitacora.setRowHeight(0,10)
        self.tablaBitacora.setRowHeight(1,50)
        self.tablaBitacora.setRowHeight(2,90)

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


    def verificarCantidadDeFilas(self,tabla,datos):
        if len(datos) > tabla.rowCount():
            tabla.setRowCount(len(datos))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MemoriaDinamica()
    main.show()
    app.exec_()