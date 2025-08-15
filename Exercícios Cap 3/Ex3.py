nome = input("Digite o nome do aluno: ")
media = int(input("Digite a média do aluno: "))

aluno = {
    "nome": nome,
    "media": media,
    "situacao": "AP" if media >= 50 else "RP"
}

print(aluno)
