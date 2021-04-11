class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        
        if (self.a == self.b) and (self.a == self.c):
            return "equilátero"
        elif (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
            return "isóceles"
        else:
            return "escaleno"
        
    def retangulo(self):
        lados = [ self.a , self.b , self.c ]

        for i in range(len(lados)):
            for j in range(len(lados)):
                if lados[i] > lados[j]:
                    lados[i], lados[j] = lados[j], lados[i]
        if (lados[0] ** 2) == ((lados[1] ** 2)+(lados[2] ** 2)):
            return True
        else:
            return False

    def semelhantes(self, t2):
        conta1 = self.a/t2.a
        conta2 = self.b/t2.b
        conta3 = self.c/t2.c

        if (conta1 == conta2) and (conta1 == conta3):
            return True
        else:
            return False
        

def teste():
    t = Triangulo(2,2,2)
    
    print(t.perimetro())
    print(t.tipo_lado())
    print(t.retangulo())

    t2 = Triangulo(4,4,4)

    print(t.semelhantes(t2))
