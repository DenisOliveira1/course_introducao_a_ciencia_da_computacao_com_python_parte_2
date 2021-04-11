def busca(lista,x):
    primeiro = 0
    ultimo = len(lista)-1
    meio = 0

    while primeiro <= ultimo:
        meio_antigo = meio
        meio = (primeiro + ultimo) // 2
        if meio != meio_antigo:
            #print("p: "+str(primeiro))
            #print("u: "+str(ultimo))
            print(meio)
        if lista[meio] == x:
            return meio
        elif x < lista[meio]:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
    return False
    
def teste():
    print("return: ",busca(['a', 'e', 'i'], 'e'))
    print("return: ",busca([1, 2, 3, 4, 5], 6))
    print("return: ",busca([1, 2, 3, 4, 5, 6], 4))
    
    
