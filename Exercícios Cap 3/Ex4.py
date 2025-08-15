nome = input("Digite o nome da primeira pessoa: ")
peso = float(input("Digite o peso da primeira pessoa: "))

mais_pesada = nome
menos_pesada = nome
peso_maior = peso
peso_menor = peso

for i in range(4):
    nome = input("Digite o nome da próxima pessoa: ")
    peso = float(input("Digite o peso da próxima pessoa: "))

    if peso > peso_maior:
        peso_maior = peso
        mais_pesada = nome
    if peso < peso_menor:
        peso_menor = peso
        menos_pesada = nome

print("Pessoa mais leve:", menos_pesada)
print("Pessoa mais pesada:", mais_pesada)
