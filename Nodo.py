class Nodo:
    def __init__(self,nombre=None,siguiente=None):
        self.nombre = nombre
        self.tamanioTotal = 0
        self.siguiente=siguiente
        self.tamanioUtilizado=0
        self.tamanioRestante=0


    def getObjeto(self):
        return self.objeto

    def getSiguiente(self):
        return self.siguiente

    def getTamanio(self):
        return self.tamanio

    def setObjeto(self,objeto):
        self.objeto=objeto

    def setSiguiente(self,siguiente):
        self.siguiente=siguiente

    def setTamanio(self,tamanio):
        self.tamanio = tamanio


[{nombre:"A",tamaño:"1MB"},{nombre:"B",tamaño:"3MB"}]

[["A",5],["A",5]]






