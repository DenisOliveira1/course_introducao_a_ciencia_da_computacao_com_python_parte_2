def conta_letras(frase,contar="vogais"):
    r = 0
    frase = frase.replace(" ","")

    if contar == "vogais":
        for letra in frase:
            if (ord(letra) == ord("a")) or (ord(letra) == ord("A")):
                r += 1
            elif (ord(letra) == ord("e")) or (ord(letra) == ord("E")):
                r += 1
            elif (ord(letra) == ord("i")) or (ord(letra) == ord("I")):
                r += 1
            elif (ord(letra) == ord("o")) or (ord(letra) == ord("O")):
                r += 1
            elif (ord(letra) == ord("u")) or (ord(letra) == ord("U")):
                r += 1
    elif contar == "consoantes":
            
        for letra in frase:
            valido = True
            
            if (ord(letra) >= ord("A")) and (ord(letra) <= ord("z")):

                if (ord(letra) == ord("a")) or (ord(letra) == ord("A")):
                    valido = False
                elif (ord(letra) == ord("e")) or (ord(letra) == ord("E")):
                    valido = False
                elif (ord(letra) == ord("i")) or (ord(letra) == ord("I")):
                    valido = False
                elif (ord(letra) == ord("o")) or (ord(letra) == ord("O")):
                    valido = False
                elif (ord(letra) == ord("u")) or (ord(letra) == ord("U")):
                    valido = False
            if valido:
                r += 1
                #print(letra+" "+str(ord(letra)))
    return r
                

def teste():
    teste1 = "programamos em python"

    print(conta_letras(teste1))
    print(conta_letras(teste1,"vogais"))
    print(conta_letras(teste1,"consoantes"))
