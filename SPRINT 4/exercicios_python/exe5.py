import csv
arquivo = 'estudantes.csv'

with open(arquivo, 'r') as arquivo:
    leitura = csv.reader(arquivo)
    next(leitura)
    listOrd = sorted(leitura)

    for l in listOrd:
        nome = l[0]
        notas = list(map(float, l[1:]))
        notasmai = sorted(notas, reverse=True)[:3]
        media = round(sum(notasmai) / len(notasmai), 2)
        notasmai_int = [int(nota) for nota in notasmai]
        media_formatada = f"{media:.2f}" if media % 1 != 0 else f"{media:.1f}"
        print(f'Nome: {nome} Notas: {notasmai_int} Média: {media_formatada}')