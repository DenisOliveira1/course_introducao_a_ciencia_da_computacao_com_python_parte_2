def encontra_impares(lista):

    if len(lista) > 0:      

        if lista[0] % 2 == 0:
            return encontra_impares(lista[1:])
        
        elif lista[0] % 2 != 0:
            return [lista[0]] + encontra_impares(lista[1:])

    return lista
    


def teste():

    lista = [-2, -7, -4]
    print(encontra_impares(lista))
