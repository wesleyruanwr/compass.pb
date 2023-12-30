import hashlib

while True:
    str = input("Digite uma string (ou pressione Enter para sair): ")
    if not str:
        break

    sha1_hash = hashlib.sha1(str.encode()).hexdigest()
    print("Hash SHA-1 da string:", sha1_hash)


print("Programa encerrado.")
