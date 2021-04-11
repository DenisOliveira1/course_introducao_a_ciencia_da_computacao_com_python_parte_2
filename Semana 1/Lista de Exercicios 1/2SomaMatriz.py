def dimensoes(m):
    linhas = len(m)
    colunas = len(m[0])
    r = []

    r.append(linhas)
    r.append(colunas)
    
    return r

def soma_matrizes(m1,m2):

    r1 = dimensoes(m1)
    r2 = dimensoes(m2)
    #sao de tamahos iguais?
    if r1 == r2:
        
        m3 = []
        for i in range(r1[0]):
            # cria linha
            linha = []

            for j in range(r1[1]):
                #enche linha
                linha.append(int(m1[i][j]) + int(m2[i][j]))
            #adiciona linha
            m3.append(linha);

        return m3
    else:
        return False
        
