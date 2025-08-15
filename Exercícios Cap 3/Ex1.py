# Leitura dos nomes dos 5 primeiros colocados
times = [input() for _ in range(5)]

# Leitura do time a ser pesquisado
pesquisa = input()

# Exibe os 3 primeiros colocados
print("\nOs 3 primeiros colocados sao:")
for time in times[:3]:
    print(time)

# Exibe os 2 últimos colocados
print("\nOs 2 ultimos colocados sao:")
for time in times[-2:]:
    print(time)

# Exibe os times em ordem alfabética
print("\nTimes em ordem alfabetica:")
for time in sorted(times):
    print(time)

# Mostra a posição do time pesquisado
posicao = times.index(pesquisa) + 1
print(f"\nO {pesquisa} esta na posicao {posicao}")
