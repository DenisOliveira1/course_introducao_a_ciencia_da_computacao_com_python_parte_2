import pytest

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista)//2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo,lado_direito)

def merge(lado_esquerdo, lado_direito):
    
    if not lado_esquerdo:#se lado esquerdo estiver vazio
        return lado_direito
    
    if not lado_direito:#se lado direito estiver vazio
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]]+merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]]+merge(lado_esquerdo, lado_direito[1:])

@pytest.mark.parametrize("entrada,esperado",[
    ([9,7,0,2,6,3,4,1,5,8],[0,1,2,3,4,5,6,7,8,9])
    ])

def test_merge(entrada,esperado):
            assert merge_sort(entrada) == esperado
