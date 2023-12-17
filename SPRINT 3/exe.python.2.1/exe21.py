class Passaro:
    def voar(self):
        print('Voando...')
    
    def emitir_som(self):
        print('Passaro gritando')

class Pato (Passaro):
    def nome(self):
        print(Pato)
    
    def emitir_som(self):
        print('Pato emitindo som...')
        print('Quack Quack')
        
class Pardal (Passaro):
    def nome(self):
        print(Pato)
    
    def emitir_som(self):
        print('Pardal emitindo som...')
        print('Piu Piu')

pato = Pato()
pardal = Pardal()

pato.nome()
pato.voar()
pato.emitir_som()
pardal.nome()
pardal.voar()
pardal.emitir_som()
