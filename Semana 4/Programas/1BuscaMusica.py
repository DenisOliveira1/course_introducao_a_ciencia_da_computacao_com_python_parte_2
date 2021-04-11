class Musica:
    def __init__(self, titulo, cantor, compositor, ano):
        self.titulo = titulo
        self.cantor = cantor
        self.compositor = compositor
        self.ano = ano

class Buscador:
    def busca_por_titulo(self, lista, alvo):
        for i in range(len(lista)):
            if lista[i].titulo == alvo:
                return i
        return -1


    def vamos_buscar(self):
        playlist = [
                    Musica("a1","a2","a3",2000),
                    Musica("b1","b2","b3",2000),
                    Musica("c1","c2","c3",2000)
                    ]

        onde_achou = self.busca_por_titulo(playlist,"a1")
        self.imprimir(playlist,onde_achou)
        onde_achou = self.busca_por_titulo(playlist,"b1")
        self.imprimir(playlist,onde_achou)
        onde_achou = self.busca_por_titulo(playlist,"d1")
        self.imprimir(playlist,onde_achou)

    def imprimir(self,playlist, onde_achou):

        if onde_achou == -1:
            print("Nao achou a musica!")
        else:
            preferida = playlist[onde_achou]
            print("Achou!",end = " ")
            print(preferida.titulo, preferida.cantor, preferida.compositor, preferida.ano)

b = Buscador()
b.vamos_buscar()





