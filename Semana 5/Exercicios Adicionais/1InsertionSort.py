def insertion_sort(lista):
   for i in range(1,len(lista)):

        ultimo_sorted = lista[i]#ultimo ordenado
        pos = i#pos = ultimo ordenado

        #enquanto pos>0  e lista
        while (pos > 0) and lista[pos-1] > ultimo_sorted:
            lista[pos] = lista[pos - 1]
            pos -= 1
            
        lista[pos] = ultimo_sorted

     

def teste():
    lista = [54,26,93,17,77,31,44,55,20]
    insertion_sort(lista)
    print(lista)
        
