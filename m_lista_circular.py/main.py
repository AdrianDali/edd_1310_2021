from lista_circular import CircleList

lista = CircleList()

print(f"La Lista esta vacia?: {lista.is_empty()}")
lista.insert(8)
lista.insert(9)
lista.insert(10)
lista.insert(11)

#lista.insert(8)
lista.transversal()
lista.search(12)



