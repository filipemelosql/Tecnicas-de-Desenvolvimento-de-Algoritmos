# Esse arquivo faz o cadastro de alunos.
# A ideia é simples: perguntar o nome até a pessoa digitar 'sair',
# guardar tudo numa lista e no final mostrar quem foi cadastrado.

def cadastrar_alunos():
    # lista vazia pra começar, aqui vão entrar todos os nomes
    alunos = []

    while True:
        # pede o nome de um aluno
        nome = input("Nome do aluno (ou 'sair' para encerrar): ")

        # se a pessoa digitar 'sair', a gente encerra o cadastro
        if nome.lower() == "sair":
            break

        # se não for 'sair', joga o nome pra dentro da lista
        alunos.append(nome)

    print("\nAlunos cadastrados:")
    # percorre a lista e imprime aluno por aluno
    for a in alunos:
        print("-", a)
