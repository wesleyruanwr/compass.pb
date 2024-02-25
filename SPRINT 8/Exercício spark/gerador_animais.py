animais = ["cachorro", "gato", "pássaro", "leão", "elefante", 
           "tigre", "girafa", "macaco", "cobra", "coelho", 
           "urso", "panda", "zebra", "jacaré", "hipopótamo",
           "águia", "pinguim", "baleia", "peixe", "aranha"]

animais_ord = sorted(animais)

print("Animais em ordem crescente:")
[print(animal) for animal in animais_ord]

nome_arquivo = "animais.csv"
with open(nome_arquivo, "w") as arquivo:
    for animal in animais_ord:
        arquivo.write(animal + "\n")

print(f"{nome_arquivo} salvo!")
