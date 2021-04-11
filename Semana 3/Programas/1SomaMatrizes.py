import ModuloCriaMatriz

def soma_matrizes(a, b):

    num_lin = len(a)
    num_col = len(a[0])
    
    c = ModuloCriaMatriz.cria_matriz(num_lin, num_col, 0)

    for lin in range(num_lin):
        for col in range (num_col):

            c[lin][col] = a[lin][col] + b[lin][col]

    return c

def teste():
    a = [[1,2,3],[4,5,6],[7,8,9]]
    b = [[10,20,30],[40,50,60],[70,80,90]]

    print(soma_matrizes(a,b))
            
