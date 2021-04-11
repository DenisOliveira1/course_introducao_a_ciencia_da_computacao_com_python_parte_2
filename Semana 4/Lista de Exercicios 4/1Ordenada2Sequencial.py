def ordenada(lista):
    for i in range (len(lista)-1):
        #print(str(i)+": "+str(lista[i])+" "+str(lista[i+1]))
        if lista[i] > lista[i+1]:         
            return False
    return True

def busca(lista, elemento):
    for i in range (len(lista)):
        if (elemento == lista[i]):
            return i
    return False
    

def teste():
    lista1 = [1,2,3,4,5,6]
    lista2 = [10,5,3,7,5,9]
    lista3 = [1,2,3,0]

    print(ordenada(lista1))
    print(ordenada(lista2))
    print(ordenada(lista3))

    print(busca(lista3,0))
    print(busca(lista3,5))
    
