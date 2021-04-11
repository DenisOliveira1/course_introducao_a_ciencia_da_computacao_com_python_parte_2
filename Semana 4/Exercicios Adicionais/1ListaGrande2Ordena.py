from random import *

def lista_grande(n):
    lista = []
    
    for i in range(n):
        lista.append(randint(0,100))

    return lista

def ordena(lista):
    for i in range(len(lista)-1):
        minimo = i
        for j in range(i+1,len(lista)):
            if lista[j] < lista[minimo]:
                lista[j], lista[minimo] = lista[minimo], lista[j]
    return lista
        

def teste():

    saida = lista_grande(30)
    print(saida)
    print(ordena(saida))
