import pytest

def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n-1)

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@pytest.mark.parametrize("entrada,esperado",[
    (0,1),
    (1,1),
    (2,2),
    (3,6),
    (4,24),
    (5,120)
    ])

def test_fatorial(entrada,esperado):
    assert fatorial(entrada) == esperado

@pytest.mark.parametrize("entrada,esperado",[
    (0,0),
    (1,1),
    (2,1),
    (3,2),
    (4,3),
    (5,5)
    ])

def test_fibonacci(entrada,esperado):
    assert fibonacci(entrada) == esperado




