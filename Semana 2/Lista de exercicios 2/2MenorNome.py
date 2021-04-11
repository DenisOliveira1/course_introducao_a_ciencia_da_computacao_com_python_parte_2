def menor_nome(listaNomes):
    menor = listaNomes[0].strip()
    
    for nome in listaNomes:
        if len(nome.strip()) < len(menor):
            menor = nome.strip()
        
    return menor.capitalize()

def teste():

    teste1 = ["maria","josé","PAULO","Catarina"]
    print(menor_nome(teste1))
