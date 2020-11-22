class Nodo:
    def __init__(self, value, siguiente = None):
        self.data = value  #falta encapsulamiento
        self.siguiente = siguiente

class LinkedList:
    def __init__(self):
        self.__head = None
        
    def is_empty(self):
        return self.__head==None

    def append(self,value):
        nuevo = Nodo(value)
        if self.__head == None: #self.is_empty()
            self.__head = nuevo
        else:
            curr_node = self.__head
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo 

    def tail(self):
        curr_node = self.__head
        while curr_node.siguiente != None:
            curr_node = curr_node.siguiente
        return curr_node

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -->", end="")
            curr_node = curr_node.siguiente
        print(" ")        

    def remove(self,value):     #elimina la primer coincidencia de el numero osea el primer numero que se encuentre
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.siguiente
        else:    
            anterior = None
            while curr_node.data != value and curr_node.siguiente !=  None:
                anterior = curr_node
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente = curr_node.siguiente
            else:
                print("el dato no existe en la lista")    

    def preppend(self, value):
        nuevo = Nodo(value, self.__head)
        self.__head = nuevo

    def get( self, posicion=None): #por defecto regresa el ultimo
        curr_node = self.__head
        contador = 0
        dato = None
        if posicion == None:
            dato = self.tail().data
        else:
            while curr_node != None:
                curr_node = curr_node.siguiente 
                contador = contador + 1
            curr_node = self.__head  
            if (posicion <= contador):
                for x in range(posicion):    #codigo aqui para verificar que esta en los limites de mi lista actual
                    curr_node = curr_node.siguiente #aqui va un ciclo donde regresamos la posicion  
                dato = curr_node.data     
                return dato
            else:
                return print("ingrese un numero en el rango")       

