def mult_matrizes(a, b):

    num_lin_A = len(a)
    num_col_A = len(a[0])

    num_lin_B = len(b)
    num_col_B = len(b[0])

    #numero de colunas de A tem que ser igual ao numero de linhas de B
    assert num_col_A == num_lin_B

    #a medida que fria a matriz resultante ja vai colcoando os resultados
    c = []

    for linha in range(num_lin_A):
        
        c.append([]) #adiciona uma linha
        for coluna in range (num_col_B):

            c[linha].append(0)#adiciona uma coluna
            for k in range(num_col_A):

                c[linha][coluna] += a[linha][k] * b[k][coluna]#sobreescreve com o valor

    return c

def teste():
    a = [[1,2,3],[4,5,6]]
    b = [[1,2],[3,4],[5,6]]

    print(mult_matrizes(a,b))
    
if __name__ == "__main__":
    teste()
      
