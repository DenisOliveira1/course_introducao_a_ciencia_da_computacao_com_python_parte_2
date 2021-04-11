import pytest

def busca_binaria(lista, x, min=0, max=None):
    #print("int")
    if max == None:
        max = len(lista)-1
        
    if max < min:
        return False
    else:
        meio = (min + max)//2
        #print(meio)
        
    if lista[meio] > x:
        return busca_binaria(lista, x, min, meio-1)
    elif lista[meio] < x:
        return busca_binaria(lista, x, meio+1, max)
    else:
        return meio
              
a = [10,20,30,40,50,60,70,80,90]

@pytest.mark.parametrize("lista, procurando,esperado",[
    (a,10,0),
    (a,20,1),
    (a,30,2),
    (a,40,3),
    (a,50,4),
    (a,60,5),
    (a,70,6),
    (a,80,7),
    (a,90,8),
    (a,100,False)
    ])

def test_busca_binaria(lista,procurando,esperado):
    assert busca_binaria(lista,procurando) == esperado

def teste():
    print(busca_binaria([10,20,30,40,50,60,70,80,90],90))
    print(a)
