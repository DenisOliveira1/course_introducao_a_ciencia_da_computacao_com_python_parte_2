def maiusculas(frase):
    r = ""
    
    for letra in frase:
        if (ord(letra) >= 65) and (ord(letra) <= 90):
            r+=letra

    return r

def teste():
    teste1 = "ashsaDWQdwDAsdwsdsdaYsaasdRdasasd"
    return maiusculas(teste1)
   
