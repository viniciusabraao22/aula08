# Passo 1: Criar a lista e preenchê-la com nomes dos alunos
alunos = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    alunos.append(nome)

# Passo 2: Mostrar os nomes e suas posições (opcional, mas ajuda na visualização)
print("\nLista de alunos e suas posições:")
for i in range(len(alunos)):
    print(f"Posição {i + 1}: {alunos[i]}")

# Passo 3: Perguntar ao usuário o nome que ele quer procurar
buscar = input("\nDigite o nome do aluno que deseja procurar: ")

# Passo 4: Procurar o nome na lista
if buscar in alunos:
    posicao = alunos.index(buscar)  # encontra o índice do nome
    print(f"{buscar} foi encontrado na posição {posicao + 1}.")
else:
    print(f"{buscar} não foi encontrado na lista.")