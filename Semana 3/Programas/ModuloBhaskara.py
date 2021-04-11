import math

class Bhaskara:

        def main(self):
            a = float(input("Digite a:"))
            b = float(input("Digite b:"))
            c = float(input("Digite c:"))
            
            print(self.calcula_raizes(a,b,c))
            
        def delta(self,a,b,c):
            return b**2 - 4 * a * c
        
        def calcula_raizes(self,a,b,c):
            d = self.delta(a,b,c)

            if d == 0:
                raiz1 = (-b + math.sqrt(d))/(2*a)
                return 1, raiz1
            
            elif d < 0:
                return 0

            else:
                raiz1 = (-b + math.sqrt(d))/(2*a)
                raiz2 = (-b - math.sqrt(d))/(2*a)
                return 2, raiz1, raiz2

#b = Bhaskara()
#b.main()            
                
                
