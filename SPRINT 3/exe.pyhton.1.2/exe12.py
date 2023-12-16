import json

with open('person.json', 'r') as arquivo_json:  #o 'r' coloca o arquivo em modo leitura
    dados = json.load(arquivo_json)
    print(dados)

