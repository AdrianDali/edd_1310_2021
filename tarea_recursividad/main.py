from pilas import Stack

def cuenta_regresiva(num):
    num -= 1
    if num > 0:
        print (num)
        cuenta_regresiva(num)    

def elim_pos_media(pila, size, curr) :
    if (pila.is_empty() or curr == size) :
        return
    x = pila.peek()
    pila.pop()
    elim_pos_media(pila, size, curr+1)
    m=(size/2)
    if m == int(m):
        if (curr != m and curr != (m-1)):
            pila.push(x)
    else:
        if (curr != int(size/2)) :
            pila.push(x)  
    
    


if __name__ == '__main__':
    cuenta_regresiva(5)
    pila = Stack()
    pila.push(9)
    pila.push(6)
    pila.push(3)
    pila.push(2)
    
    print(pila.to_string())
    l = pila.length()

    elim_pos_media(pila,l,0)
