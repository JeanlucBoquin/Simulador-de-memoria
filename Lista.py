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
            print(nodoActual.tamanioTotal)
            nodoActual=nodoActual.siguiente

#################Metodos para particonamiento fijo del mismo tamanio#############################3   

    def hacerParticionesMismoTamanioFijo(self,numeroParticones):
        tamanioParticionesFinal= self.memoriaDisponoble/numeroParticones
        for i in range(0,numeroParticones):
            self.agregar("",tamanioParticionesFinal)
    
    def cargarProcesoMismoTamanioFijo(self,nombre,tamanio):
            nodoActual=self.nodo
            while nodoActual:
                if(nodoActual.nombre==nombre):
                    break
                if(nodoActual.tamanioTotal >= tamanio):
                    nodoActual.nombre=nombre
                    nodoActual.tamanioUtilizado=tamanio
                    nodoActual.tamanioRestante=nodoActual.tamanioTotal - nodoActual.tamanioUtilizado
                    break
                nodoActual=nodoActual.siguiente
    
    def liberarProcesosMismoTamanioFijo(self, nombre):
        nodoActual=self.nodo
        while nodoActual:
            if(nombre == nodoActual.nombre):
                nodoActual.nombre = ""
                nodoActual.tamanioUtilizado=0
                nodoActual.tamanioRestante=nodoActual.tamanioTotal - nodoActual.tamanioUtilizado
            nodoActual=nodoActual.siguiente
    
            
################Metodos para el partcionamiento fijo de diferente tamanio##########

    def hacerParticionesDeDiferenteTamnio(self):
        particiones =[15,1,8,3,10,4,14,2,5]
        for i in range(0,len(particiones)):
           self.agregar("",particiones[i])
    
    def cargarProcesoDistintoTamanioFijo(self,nombre,tamanio):
        self.cargarProcesoMismoTamanioFijo(nombre,tamanio)

    def liberarProcesoDistintoTamanioFijo(self, nombre):
        self.liberarProcesosMismoTamanioFijo(nombre)

################Metodos para el partcionamiento dinámico##########

    def liberarProceso_PartDinamico(self, nombre):
        nodoActual = self.nodo
        while nodoActual:
            if (nodoActual.nombre == nombre):
                nodoActual.nombre = ""
            nodoActual = nodoActual.siguiente
    
    def cargarProceso_PartDinamico_MejorAjuste(self, nombre, tamanio):
        pass