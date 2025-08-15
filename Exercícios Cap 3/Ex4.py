# Faça um programa que leia o nome e peso de 5 pessoas e no final mostre os nomes da pessoa mais pesada e da mais leve.

# Entrada
# A entrada consiste de 6 linhas:

# A primeira linha contém o nome da primeira pessoa

# A segunda linha contém o peso da primeira pessoa (um número real)

# A terceira linha contém o nome da segunda pessoa

# A quarta linha contém o peso da segunda pessoa

# e assim por diante.

# Saída
# Na saída, o programa deve mostrar os nomes da pessoa mais pesada e da pessoa mais leve, conforme o exemplo abaixo.

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
