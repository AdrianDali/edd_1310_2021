from arbol_binario import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(15)
abb.insert(23)
abb.insert(110)
abb.insert(90)
abb.insert(120)
abb.insert(100)
abb.insert(55)
abb.insert(58)
abb.insert(115)

abb.transversal()
abb.remove(120)
abb.transversal()
# abb.transversal()
# abb.transversal("preorden")
# abb.transversal("posorden")

# abb.search(60)