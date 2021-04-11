def incomodam(n):
    p = "incomodam "

    if n <= 0:
        return ""
        
    if n == 1:
        return p

    return p + incomodam(n-1)

def elefantes(n):
    if n <= 0:
        return ""
        
    if n == 1:
        return "Um elefante incomoda muita gente"

    return elefantes(n-1) + cria_string(n)





def cria_string(n):
    string = "\n" + str(n) +" elefantes "
    
    for i in range (n):
        string = string + "incomodam "

    string = string + "muito mais\n" + str(n) + " elefantes incomodam muita gente"
        
    return string
        


def teste():
    print(incomodam(4))
    print(elefantes(4))
