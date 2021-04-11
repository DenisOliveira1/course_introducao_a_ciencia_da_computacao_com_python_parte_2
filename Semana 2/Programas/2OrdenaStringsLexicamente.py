def menor_string(m):
    for i in range (len(m)):
        for j in range (len(m)):
            if m[i].lower() < m[j].lower():
                
                #aux = m[i]
                #m[i] = m[j]
                #m[j] = aux
                
                m[i],m[j] = m[j],m[i]# mesma coisa , troca variaveis

    return m

def teste():
    
    teste1 = ["aaa","HHH","CCC","ddd","555","ggg","CCC"]
    m = menor_string(teste1)

    return m


print(teste())
        
    
