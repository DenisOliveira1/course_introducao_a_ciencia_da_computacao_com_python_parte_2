def primeiro_lex(m):
    for i in range (len(m)):
        for j in range (len(m)):
            if m[i].lower() < m[j].lower():
                
                #aux = m[i]
                #m[i] = m[j]
                #m[j] = aux
                
                m[i],m[j] = m[j],m[i]# mesma coisa , troca variaveis

    return m[0]

def teste():
    
    teste1 = ["AAAAAA","b"]
    teste2 = ["olá","A","a","casa"]
    
    print(menor_string(teste1))
    print(menor_string(teste2))
