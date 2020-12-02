
class Nodo:


    def __init__(self, value, siguiente = None):
        self.data = value 
        self.siguiente = siguiente


class CircleList:
    

    def __init__(self):
        self.__ref = None


    def is_empty(self):
        return self.__ref == None 


    def insert(self, value):
        nuevo = Nodo(value)
        curr_node = self.__ref
        if self.__ref == None:
            self.__ref = nuevo
        else:
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo


    def transversal(self):
        curr_node = self.__ref
        while curr_node != None:
            print(f"{curr_node.data} -->", end="")
            curr_node = curr_node.siguiente
        print(" ")        

    def search(self,value):
        curr_node = self.__ref
        while curr_node.data != value or curr_node.siguiente != None :
            curr_node = curr_node.siguiente
            if curr_node.data == value:
                return print(True)
            else:
                return print(False) 

    def remove(self, value):
        pass


    