def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        
        #cria a linha i
        linha = []
        for j in range(num_colunas):
            #acrescenta um valor ao final da linha atual
            valor = valor + 1
            linha.append(valor)

        #adiciona linha à matriz
        matriz.append(linha);

    return matriz;
    #return imprime(matriz);

def imprime(m):
    for a in m:
        print(a)
