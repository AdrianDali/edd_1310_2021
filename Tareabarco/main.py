from queue import Queue,BoundedPriorityQueue, PriorityQueue


cola = Queue()
cola.enqueue(3)
cola.enqueue(33)
cola.enqueue(23)
print(cola.to_string())
cola.length()
cola.dequeue()
print(cola.to_string())

print("preuba dos")
c1 = {"id" : 1, "nombre": "Mario", "balance": 20.5}
c2 = {"id" : 2, "nombre": "diana", "balance": 3265.5}
c3 = {"id" : 3, "nombre": "bartolo", "balance": 10000.5}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
#siguiente = atencion.dequeue()
print(f"Bienvenido sr en que podemos servirle el dia de hoy")
print(atencion.to_string())

print("-----------------------------------------------------")

print("Pruebas de las colas con prioridad acotada")

maestres = {"prioridad":4 , "descripcion": "Maestres", "personas":["Juan P", "Diego H"]}
niños = {"prioridad":2 , "descripcion": "Niños", "personas":["Santi J", "Angel H"]}
mecanicos = {"prioridad":4 , "descripcion": "Mecanicos", "personas":["Carlos J", "Marie V"]}
mujeres = {"prioridad":3 , "descripcion": "Mujeres" , "personas" :["Monica P" , "Carla M"]}
viejitos = {"prioridad": 2 , "descripcion": "Tercera edad" , "personas": ["Miguel A" , "Rodrigo C"]}
niñes = {"prioridad": 1 , "descripcion": "Niñas" , "personas": ["Mariana G" , "Fernanda R"]}
hombres = {"prioridad": 3 , "descripcion": "Hombres" , "personas": ["Cristian H" , "Daniel B"]}
vigia ={"prioridad": 4 , "descripcion": "Vigia" , "personas": ["Tomas B" , "Lorena O"]}
capitan = {"prioridad": 5 , "descripcion": "Capitan" , "personas": [ "Sergio B"]}
timonel  = {"prioridad": 4 , "descripcion": "Timonel" , "personas": ["Jose X"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)  
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.enqueue(viejitos['prioridad'], viejitos)
cpa.enqueue(niñes['prioridad'], niñes)
cpa.enqueue(hombres['prioridad'],hombres)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(capitan['prioridad'], capitan)
cpa.enqueue(timonel['prioridad'], timonel)

cpa.to_string()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()

print('EL BARCO HA SIDO EVACUADO\n')
cpa.to_string()

print("-----------------------------------------------------")
pq = PriorityQueue()
print(f"La cola esta vacia?  {pq.is_empty()}")
print(f"el tamaño de la cola: {pq.length()}")