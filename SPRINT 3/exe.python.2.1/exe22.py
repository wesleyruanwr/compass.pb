class Pessoa:
    def __init__(self, identificador):
        self.id = identificador
        self.__nome = None

    def nome(self):
        return self.__nome

    def nome(self, novo_nome):
        self.__nome = novo_nome

pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
