class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            posicao_do_minimo = i
            #print(i)

            for j in range(i+1,fim):
                #print("j",j)

                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

        return lista

    def bubblesort(self, lista):
        
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

        return lista

    def corrige(self, lista):

        fim = len(lista)
        
        for i in range(fim - 2):
                if lista[i] > lista[i+1]:
                    return False #nao esta ordenada
        return True #esta ordenada

    
                
                
    
lista = [10,4,15,3,8,-3,-10,-2,5,8]

o = Ordenador()

print(lista)
lista_ordenada = o.bubblesort(lista)
print(lista_ordenada)
print(o.corrige(lista_ordenada))


