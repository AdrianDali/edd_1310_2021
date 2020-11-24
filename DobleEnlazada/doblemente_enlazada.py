class NodoDoble():

    def __init__(self,value, siguiente = None, anterior = None):
        self.data = value
        self.siguiente = siguiente
        self.anterior = anterior


class DoubleLinkedList():
    def __init__(self):
        self.__head = NodoDoble(None,None,None)
        self.__tail = NodoDoble(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0 
        #print(f"head: {self.__head} ")
        #print(f"tail: {self.__tail} ")

    def is_empty(self):
        return self.__head  == None


    def get_size(self):
        curr_node = self.__head
        contador = 0
        while curr_node != None:
            curr_node = curr_node.siguiente
            contador = contador + 1
        return print(contador)    


    def append(self,value):
        curr_node = self.__head
        nuevo = NodoDoble(value)
        if self.__head == None:
            self.__head = nuevo
        else:
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo  


    def find_from_tail(self,value):
        pass


    def find_from_head(self, value):
        curr_node = self.__head
        dato = None
        for x in range(value):
            curr_node = curr_node.siguiente  
        dato = curr_node.data
        return print(dato)


    def remove_from_tail(self, value):
        pass


    def remove_from_head(self, value):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.siguiente
        else:
            anterior = None
            while curr_node.data != value and curr_node.siguiente != None:
                anterior = curr_node
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente = curr_node.siguiente
            else:
                print("el dato no existe en la lista")            


    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -->", end="")
            curr_node = curr_node.siguiente
        print(" ") 


    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f"{curr_node.data} -->", end="")
            curr_node = curr_node.anterior
        print(" ") 
