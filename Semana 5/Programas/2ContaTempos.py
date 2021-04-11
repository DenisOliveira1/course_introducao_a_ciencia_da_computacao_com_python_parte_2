from random import *
import time
import Modulo #modulo

class ContaTempos:
    
    def lista_aleatoria(self,n):
        lista = [randrange(100) for x in range(n)]
        return lista

    def lista_quase_ordenada(self,n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara (self,lista1):

        lista2 = lista1[:] #clonar lista
        lista3 = lista1[:] #clonar lista

        o = Modulo.Ordenador() #cria objeto
        antes = time.time()#inicio     
        o.bubbleSort(lista1)      
        depois = time.time()#fim
        
        resultado = depois - antes
        print("BubleSort demorou: "+str(resultado))

        antes = time.time()#inicio     
        o.bubbleSortCurta(lista2)      
        depois = time.time()#fim
        
        resultado = depois - antes
        print("BubbleSortCurta demorou: "+str(resultado))

        antes = time.time()#inicio     
        o.selecao_direta(lista3)      
        depois = time.time()#fim
        
        resultado = depois - antes
        print("SelectionSort demorou: "+str(resultado))

def teste():
    c = ContaTempos()
    n = 5000
    
    print("\nlista aleatorias\n")
    c.compara(c.lista_aleatoria(n))
    print("\nlista quase ordenada\n")
    c.compara(c.lista_quase_ordenada(n))
        
