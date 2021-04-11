def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        
        #cria a linha i
        linha = []
        for j in range(num_colunas):
            #acrescenta um valor ao final da linha atual
            linha.append( int(input("Digite o valor para a posição["+str(i)+"]["+str(j)+"]: ")))

        #adiciona linha à matriz
        matriz.append(linha);

    #return matriz;
    return imprime(matriz);

def imprime(m):
    for a in m:
        print(a)

def le_matriz():
    nLinhas =  int(input("Digite o numero de linhas da matriz: "))
    nColunas =  int(input("Digite o numero de colunas da matriz: "))
    cria_matriz(nLinhas,nColunas)

le_matriz()
