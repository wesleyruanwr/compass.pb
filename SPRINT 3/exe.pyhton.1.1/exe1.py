import datetime
nome = str(input('Nome: '))
idade = int(input('Idade: '))
anoatual = datetime.date.today().year 
datanasc = anoatual - idade
data100 = datanasc + 100
print(data100)
