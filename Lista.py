from Nodo import Nodo
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
class Lista:
    def __init__(self):
        self.nodo=None
        self.memoriaDisponoble = 56
        self.ultimoIngresado = None

    def agregar(self, nombre, tamanio,i=None):
        if self.nodo==None:
           self.nodo=Nodo(nombre,tamanio,i)
           self.ultimoIngresado = self.nodo #####
        elif self.nodo.siguiente==None:
            self.nodo.siguiente=Nodo(nombre,tamanio,i)
            if (self.nodo.siguiente.nombre != ""):
                self.ultimoIngresado = self.nodo.siguiente ####
        else:
            nodoActual=self.nodo.siguiente
            while nodoActual:
                if nodoActual.siguiente==None:
                    nodoActual.siguiente=Nodo(nombre,tamanio,i)
                    if (nodoActual.siguiente.nombre != ""):
                        self.ultimoIngresado = nodoActual.siguiente ####
                    
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
        if self.nodo == None:
            return False
        if self.nodo.nombre == nombre:
            return self.nodo
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
            print("nombre: %s   tamanio:%s   fija:%s"%(nodoActual.nombre,nodoActual.tamanioTotal,nodoActual.fila))
            # print(nodoActual.tamanioUtilizado)
            nodoActual=nodoActual.siguiente


#################Metodos para particonamiento fijo del mismo tamanio#############################3

    def hacerParticionesMismoTamanioFijo(self,numeroParticones):
        tamanioParticionesFinal= self.memoriaDisponoble/numeroParticones
        for i in range(0,numeroParticones):
            self.agregar("",tamanioParticionesFinal,i)

    def cargarProcesoMismoTamanioFijo(self,nombre,tamanio):
            nodoActual=self.nodo
            while nodoActual:
                if(nodoActual.nombre==nombre):
                    break
                if(nodoActual.tamanioTotal >= tamanio and nodoActual.nombre == ""):
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
        particiones =[14,11,20,4,7]
        for i in range(0,len(particiones)):
           self.agregar("",particiones[i],i)

    def cargarProcesoDistintoTamanioFijo(self,nombre,tamanio):
        self.cargarProcesoMismoTamanioFijo(nombre,tamanio)

    def liberarProcesoDistintoTamanioFijo(self, nombre):
        self.liberarProcesosMismoTamanioFijo(nombre)




    def reconstruirTabla(self,tabla):
        tabla.clearContents()
        tabla.setRowCount(0)
        nodoActual  = self.nodo
        if nodoActual == None:
            return
        contador = 0
        while nodoActual:
            # nodoActual.fila = contador
            tabla.insertRow(nodoActual.fila)
            tabla.setRowHeight(nodoActual.fila,40)

            print("#########")
            print("nombre:%s    tamanio:%s fila:%s"%(nodoActual.nombre,nodoActual.tamanioTotal,nodoActual.fila))
            print("#########")
            if nodoActual.nombre != "":
                tabla.setItem(nodoActual.fila, 0, QTableWidgetItem("Nombre: %s\n MU: %s"%(nodoActual.nombre,nodoActual.tamanioTotal)))
            else:
                tabla.setItem(nodoActual.fila, 0, QTableWidgetItem("ML: %s"%(nodoActual.tamanioTotal)))
            tabla.item(nodoActual.fila,0).setTextAlignment(Qt.AlignCenter)
            contador +=1 
            nodoActual = nodoActual.siguiente



################Metodos para el partcionamiento dinámico##########

    def liberarProceso_PartDinamico(self, nombre):
        nodoActual = self.nodo
        while nodoActual: #C D
            if (nodoActual.nombre == nombre):
                nodoActual.nombre = ""
                try:
                    if nodoActual.siguiente.nombre == "":
                        nodoActual.tamanioTotal += nodoActual.siguiente.tamanioTotal
                        nodoActual.siguiente = nodoActual.siguiente.siguiente
                        self.unirVacios()
                except Exception as e:
                    print("por si acaso %s"%e)
            
            nodoActual = nodoActual.siguiente
        self.unirVacios()
        # self.unirVacios()
        # self.unirVacios()

    def unirVacios(self):
        nodoActual = self.nodo
        while nodoActual:

            try:
                if nodoActual.nombre == "":
                    if nodoActual.siguiente.nombre == "":
                        nodoActual.tamanioTotal += nodoActual.siguiente.tamanioTotal
                        nodoActual.siguiente = nodoActual.siguiente.siguiente
                # nodoActual = nodoActual.siguiente
            except Exception as e:
                print("contola %s"%e)
            nodoActual = nodoActual.siguiente

    def reEnumerarFila(self):
        fila = 0
        nodoActual = self.nodo
        while nodoActual:
            nodoActual.fila = fila
            fila+=1
            print(nodoActual.fila)
            nodoActual= nodoActual.siguiente
       
    # def reEnumerar
    def cargarProceso_PartDinamico_MejorAjuste(self, nombre, tamanio):
        if ((self.nodo==None) and (tamanio <= self.memoriaDisponoble)):
            self.agregar(nombre, tamanio)
            self.agregar("", self.memoriaDisponoble-tamanio)
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!")
            #Buscando las particiones mayores o iguales libres
            nodoActual = self.nodo
            tamaniosProcesosMayoresOIguales = []
            tamanioMejorAjuste = 0
            while nodoActual:
                if (nodoActual.tamanioTotal >= tamanio and nodoActual.nombre == ""):
                    tamaniosProcesosMayoresOIguales.append(nodoActual.tamanioTotal)
                nodoActual = nodoActual.siguiente
                print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&6")
            print(tamaniosProcesosMayoresOIguales)
            tamaniosProcesosMayoresOIguales.sort()
            tamanioMejorAjuste = tamaniosProcesosMayoresOIguales[0]
            print(tamaniosProcesosMayoresOIguales)
            #Recorrer la lista buscando la partición más ajustada.
            nodoActual = self.nodo
            while nodoActual:
                if (nodoActual.nombre == nombre):
                    print("Hay el mismo nombre ya")
                    break
                else:
                    if (nodoActual.tamanioTotal == tamanioMejorAjuste and nodoActual.nombre == ""):
                        nodoActual.nombre = nombre
                        self.ultimoIngresado = nodoActual
                        if (nodoActual.tamanioTotal > tamanio):
                            tamanioQueResta = nodoActual.tamanioTotal - tamanio
                            nodoActual.tamanioTotal = tamanio
                
                            siguiente_temp = nodoActual.siguiente
                            #nodoActual.siguiente = self.agregar("", tamanioQueResta)
                            nodoActual.siguiente = Nodo("", tamanioQueResta)
                            nodoActual.siguiente.siguiente = siguiente_temp
                    break
                nodoActual = nodoActual.siguiente

    def cargarProceso_PartDinamico_PrimerAjuste(self, nombre, tamanio):
        if self.nodo==None:
            self.agregar(nombre, tamanio)
            if (tamanio != self.memoriaDisponoble):
                self.agregar("", self.memoriaDisponoble-tamanio)
        else:
            nodoActual = self.nodo
            while nodoActual:
                if(nodoActual.nombre == nombre):
                    break
                if (nodoActual.tamanioTotal >= tamanio and nodoActual.nombre == ""):
                    nodoActual.nombre = nombre
                    self.ultimoIngresado = nodoActual
                    if (nodoActual.tamanioTotal > tamanio):
                        tamanioQueResta = nodoActual.tamanioTotal - tamanio
                        nodoActual.tamanioTotal = tamanio

                        siguiente_temp = nodoActual.siguiente
                        #nodoActual.siguiente = self.agregar("", tamanioQueResta)
                        nodoActual.siguiente = Nodo("", tamanioQueResta)
                        nodoActual.siguiente.siguiente = siguiente_temp
                    break
                nodoActual = nodoActual.siguiente



    def cargarProceso_PartDinamico_SiguienteAjuste(self, nombre, tamanio): #supuestamente completo.
        if self.ultimoIngresado==None:
            self.agregar(nombre, tamanio)
            self.agregar("", self.memoriaDisponoble-tamanio)

        else:
            nodoActual=self.ultimoIngresado
            ingresadoYa = False
            while (nodoActual):
                if (nodoActual.nombre == nombre):
                    print("Hay otro nombre ya")
                    break
                if (nodoActual.tamanioTotal >= tamanio and nodoActual.nombre == ""):
                    #Adición y creación
                    nodoActual.nombre = nombre
                    self.ultimoIngresado = nodoActual
                    if (nodoActual.tamanioTotal > tamanio):
                        tamanioQueResta = nodoActual.tamanioTotal - tamanio
                        nodoActual.tamanioTotal = tamanio

                        siguiente_temp = nodoActual.siguiente
                        #nodoActual.siguiente = self.agregar("", tamanioQueResta)
                        nodoActual.siguiente = Nodo("", tamanioQueResta)
                        nodoActual.siguiente.siguiente = siguiente_temp
                    ingresadoYa = True
                if (ingresadoYa==True):
                    break
                nodoActual = nodoActual.siguiente

            if (ingresadoYa==False):
                self.cargarProceso_PartDinamico_PrimerAjuste(nombre, tamanio)