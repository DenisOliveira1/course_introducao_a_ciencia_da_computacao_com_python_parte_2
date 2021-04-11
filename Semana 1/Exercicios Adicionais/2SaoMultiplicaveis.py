def dimensoes(m):
    linhas = len(m)
    colunas = len(m[0])
    r = []

    r.append(linhas)
    r.append(colunas)
    
    return r

def sao_multiplicaveis(m1,m2):

    r1 = dimensoes(m1)
    r2 = dimensoes(m2)

    if (r1[1] == r2[0]):
        return True
    else:
        return False

def teste():

    m1 = [[1]]
    m2 = [[1,1,1]]

    print(sao_multiplicaveis(m1,m2))

