from queue import Queue,BoundedPriorityQueue


# cola = Queue()
# cola.enqueue(3)
# cola.enqueue(33)
# cola.enqueue(23)
# print(cola.to_string())
# cola.length()
# cola.dequeue()
# print(cola.to_string())

# print("preuba dos")
# c1 = {"id" : 1, "nombre": "Mario", "balance": 20.5}
# c2 = {"id" : 2, "nombre": "diana", "balance": 3265.5}
# c3 = {"id" : 3, "nombre": "bartolo", "balance": 10000.5}

# atencion = Queue()
# atencion.enqueue(c1)
# atencion.enqueue(c2)
# atencion.enqueue(c3)
# print(atencion.to_string())
# #siguiente = atencion.dequeue()
# print(f"Bienvenido sr en que podemos servirle el dia de hoy")
# print(atencion.to_string())


print("Pruebas de las colas con prioridad acotada")

maestres = {"prioridad":4, "descripcion":"Maestre","personas":["juan p","diego h"]}
niños = {"prioridad":2, "descripcion":"Niños","personas":["juan p","diego h"]}
mecanicos = {"prioridad":4, "descripcion":"Mecanicos","personas":["juan p","diego h"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.to_string()
