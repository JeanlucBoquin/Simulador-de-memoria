from Nodo import Nodo
class Lista:
    def __init__(self):
        self.nodo=None
        self.memoriaDisponoble = 56
    
    def agregar(self, nombre, tamanio):
        if self.nodo==None:
           self.nodo=Nodo(nombre,tamanio)
        elif self.nodo.siguiente==None:
            self.nodo.siguiente=Nodo(nombre,tamanio)
        else:
            nodoActual=self.nodo.siguiente
            while nodoActual:
                if nodoActual.siguiente==None:
                    nodoActual.siguiente=Nodo(nombre,tamanio)
                    break
                nodoActual=nodoActual.siguiente
        
    def eliminar(self,nombre):
        if self.nodo.nombre == nombre:
            self.nodo=self.nodo.siguiente
        else:
            nodoAnterior=self.nodo
            nodoActual=self.nodo.siguiente
            while nodoActual:
                if nodoActual.nombre==nombre:
                    nodoAnterior.siguiente=nodoActual.siguiente
                    break
                nodoAnterior=nodoActual
                nodoActual=nodoActual.siguiente

    def buscar(self,nombre):
        if self.nodo.nombre == nombre: 
            return True
        else:
            nodoActual=self.nodo.siguiente
            while nodoActual:
                if nodoActual.nombre == nombre:
                    return nodoActual
                nodoActual = nodoActual.siguiente
            return False

    def listar(self):
        nodoActual=self.nodo
        while nodoActual:
            print(nodoActual.nombre)
            nodoActual=nodoActual.siguiente