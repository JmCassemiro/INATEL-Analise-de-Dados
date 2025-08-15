
# bibliotecas
import math  # Biblioteca matemática
# import random  # Biblioteca para gerar números aleatórios


# comandos basicos de python
print('Hello, World!')
print(7 + 7)
print('O resultado de 7 + 7 é:', 7 + 7)  # para imprimir mais de uma coisa usamos virgulas

nome = 'henrique'
idade = 20
peso = 70.5

print(f'Seu nome é: {nome}, voce tem {idade} anos, e pesa {peso:.2f} kg')
# f-string para formatar strings/ :.2f para limitar a 2 casas decimais
print('Meu nome é', nome, 'tenho', idade, 'anos e peso', peso, 'kg')

# leitura de dados
# nome = input('Qual é o seu nome? ')
# idade = int(input('Qual é a sua idade? '))
# peso = float(input('Qual é o seu peso? '))

print(f'Seu nome é: {nome}, voce tem {idade} anos, e pesa {peso:.2f} kg')

print(type(nome))  # Verifica o tipo da variável nome
print(type(idade))  # Verifica o tipo da variável idade
print(type(peso))  # Verifica o tipo da variável peso

# operadores aritmeticos

# x = int(input())
# y = int(input())
x = 10
y = 3
soma = x + y
diferença = x - y
produto = x * y
quociente = x / y
resto = x % y
potencia = x ** y
divisaointeira = x // y

print('A soma é:', soma)
print('A diferença é:', diferença)
print('O produto é:', produto)
print('O quociente é:', f'{quociente:.2f}')
print('O resto é:', resto)
print('A potenciação é:', potencia)

# x = float(input())
x = 7.8
print(math.trunc(x))  # Usando a função trunc da biblioteca math

print(math.ceil(x))  # Arredonda para cima
print(math.floor(x))  # Arredonda para baixo
print(round(x))  # Arredonda para o inteiro mais próximo

# cadeias de caracteres

var = 'Python é uma linguagem de programação'
print(var[0])
print(var[6:11])  # Imprime a substring da posição 6 até 11
print(var[6:])  # Imprime a substring da posição 6 até o final
print(var[0:11:2])  # Imprime a substring da posição 0 até 11, pulando de 2 em 2

# funcoes uteis

var = 'Hello World'
print(len(var))  # Imprime o tamanho da string
print(var.lower())  # Converte para minúsculas
print(var.upper())  # Converte para maiúsculas
print(var.replace('World', 'Python'))  # Substitui 'World' por 'Python'
print(var.split())  # Divide a string em uma lista de palavras
print('World' in var)  # Verifica se 'World' está na string
print(var.count('o'))  # Conta quantas vezes 'o' aparece na string
print(var.count('l', 0, 5))  # Conta quantas vezes 'l' aparece na string, do início até a posição 5
print(var.find('World'))  # Encontra a posição de 'World' na string
print(var.index('World'))  # Encontra a posição de 'World' na string
print(var.startswith('Hello'))  # Verifica se a string começa com 'Hello'
print(var.endswith('World'))  # Verifica se a string termina com 'World'
print(var.isalpha())  # Verifica se a string contém apenas letras
print(var.isalnum())  # Verifica se a string contém apenas letras e números
print(var.isdigit())  # Verifica se a string contém apenas dígitos
