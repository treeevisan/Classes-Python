
class TV:

# Atributo de classe --> Inalteravel
    self.cor = 'preta'

    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal




salatv = TV(55)

print(salatv.tamanho)


