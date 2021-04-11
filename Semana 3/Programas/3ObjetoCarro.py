#construtor
class Carro:
    def __init__(self, modelo, ano, cor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("gto",2000,"azul")
carro2 = Carro("eclipse",2000,"vermelho")

#lista com os objetos Carro
carros = [carro1,carro2]

print(carro1.modelo+" "+carro1.cor)
carro1.cor = "verde"
print(carro1.modelo+" "+carro1.cor)


