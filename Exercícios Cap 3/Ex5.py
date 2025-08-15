n = int(input("Digite o número de pessoas: "))

soma_idade = 0
cont_mulheres_menor_20 = 0

for i in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (homem/mulher): ")

    soma_idade += idade

    if sexo == "mulher" and idade < 20:
        cont_mulheres_menor_20 += 1

media_idade = soma_idade / n

print("Média de idade:", media_idade)
print("Mulheres com menos de 20 anos:", cont_mulheres_menor_20)
