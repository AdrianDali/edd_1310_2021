from arbol_binario import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)
abb.insert(70)
abb.insert(25)


abb.transversal()
abb.transversal("preorden")
abb.transversal("posorden")

abb.search(60)