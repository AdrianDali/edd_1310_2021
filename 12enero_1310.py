def factorial(numero):
    if numero == 0:
        return 1 
    return numero * factorial(numero-1)

def printRev(numero):
    if numero > 0:
        
        printRev(numero - 1)  
        print(numero)  

def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return (fibonacci(numero-1) + fibonacci(numero-2))  

def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)
              

if __name__ == "__main__":
    numero = int(input("Ingresa un numero: "))
    resultado = factorial(numero)
    print(f"el resultado es: {resultado}")
    print(printRev(9))
    print("-------------------------")
    print(fibonacci(4))
    print("-------------------------")
    datos = [4,2,3,5]
    r = suma_lista_rec(datos)
    print(r)

