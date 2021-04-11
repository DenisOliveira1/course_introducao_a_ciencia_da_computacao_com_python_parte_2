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


def teste():
    print(fatorial(2))
    print(fatorial(4))
    print(fatorial(10))
