# Lê os valores de entrada
n = int(input())       # número da tabuada
inicio = int(input())  # início do intervalo
fim = int(input())     # fim do intervalo

# Caso o início seja maior que o fim, invertemos para evitar erro
if inicio > fim:
    inicio, fim = fim, inicio

# Gera a tabuada no intervalo
for i in range(inicio, fim + 1):
    print(f"{n} x {i} = {n * i}")
