class Aviao:
    cor = "Azul"

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

lista_avioes = []
entradas = [
    "modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul",
    "modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul",
    "modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul"
]

for entrada in entradas:
    partes = entrada.split(":")
    modelo = partes[0].split()[1]