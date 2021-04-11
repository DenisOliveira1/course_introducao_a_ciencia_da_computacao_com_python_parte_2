class Buscador:
    def busca_sequencial(self,lista,x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1
    
    def busca_binaria(self,lista,x):
        primeiro = 0
        ultimo = len(lista)-1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            #print("primeiro: "+str(primeiro)+" + "+"ultimo: "+str(ultimo))
            #print("meio: "+str(meio))
            if lista[meio] == x:
                return meio
            elif x < lista[meio]:
                ultimo = meio-1
            else:
                primeiro = meio + 1
        return -1


def teste():
    #lista = [-50,-40,-30,-20,-10,10,20,30,40,50,60,80,90]
    lista = [3, 6, 12, 13, 17, 18, 43]
    print(lista)
    b = Buscador()
    print(b.busca_binaria(lista,8))
    print(b.busca_binaria(lista,10))
    print(b.busca_binaria(lista,15))
    print(b.busca_binaria(lista,20))
    
    
