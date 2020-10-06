class Nodo:
    def __init__(self,nombre,tamanio):
        self.nombre = nombre
        self.tamanioTotal = tamanioTotal
        self.siguiente=None
        self.tamanioUtilizado=0
        self.tamanioRestante=0
        self.fila=i
        self.rightChild = None
        self.leftChild  = None
    
    def setValue(self,value):
        self.value=value    
    
    def getValue(self): 
        return self.value

class BST():
    def __init__(self):
        self.root = None
    
    def setRoot(self,value):
        self.root=Nodo(value)
    
    def add(self,value):
        if self.root is None:
            self.setRoot(value)
            
        else:
            self.addInner(self.root,value)
    
    def addInner(self,currentNodo,value):
        if currentNodo.value >= value:
            if currentNodo.leftChild is not None:
                self.addInner(currentNodo.leftChild,value)
            else:
                currentNodo.leftChild = Nodo(value)

        else:
            if currentNodo.rightChild is not None:
                self.addInner(currentNodo.rightChild,value)
            else:
                currentNodo.rightChild = Nodo(value)

    def search(self,value):             
        return self.searchInner(self.root,value)

    def searchInner(self,currentNodo,value):

        if currentNodo is None:
        	return False
        elif currentNodo.value == value:
        	return True
        elif currentNodo.value > value:
        	return self.searchInner(currentNodo.leftChild,value)
        else:    
        	return self.searchInner(currentNodo.rightChild,value)    




arbol1 = BST()       

arbol1.add(10)
arbol1.add(25)
arbol1.add(30)
arbol1.add(15)
arbol1.add(100)

print arbol1.search(10)


