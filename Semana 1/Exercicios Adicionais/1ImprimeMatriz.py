def imprime_matriz(m):
    espaco = False
    
    for linha in m:
        for numero in linha:
            if espaco:
                print(" ",end="")
            print(str(numero),end="")
            espaco = True
        espaco = False       
        print("")
