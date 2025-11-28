# Programa: Cadastro de nomes de alunos
# Disciplina: Técnicas de Desenvolvimento de Algoritmos
# Conteúdo: Listas
# Autor: Filipe Melo

# Este programa permite cadastrar vários nomes de alunos em uma lista.
# O usuário digita os nomes e, quando terminar, digita 'sair'.
# Ao final, todos os nomes cadastrados são exibidos.

# Criação da lista vazia para armazenar os nomes
alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")

    # Se o usuário digitar 'sair', encerramos o cadastro
    if nome.lower() == "sair":
        break

    # Adiciona o nome digitado à lista de alunos
    alunos.append(nome)

print("\nLista final de alunos cadastrados:")

# Percorre a lista e exibe cada nome
for aluno in alunos:
    print("-", aluno)

# Fim do programa
