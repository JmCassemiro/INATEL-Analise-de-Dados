# Leitura dos modelos da Loja 1
n1 = int(input())
loja1 = [input().strip() for _ in range(n1)]

# Leitura dos modelos da Loja 2
n2 = int(input())
loja2 = [input().strip() for _ in range(n2)]

# Conjuntos para operações
set_loja1 = set(loja1)
set_loja2 = set(loja2)

# União e interseção como listas ordenadas
uniao = sorted(set_loja1 | set_loja2)
intersecao = sorted(set_loja1 & set_loja2)

# Saída exatamente como esperado
print("Modelos disponiveis em pelo menos uma das lojas:")
print(uniao)

print("\nModelos disponiveis em ambas as lojas:")
print(intersecao)
