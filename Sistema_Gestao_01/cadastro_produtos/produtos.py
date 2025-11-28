# Esse arquivo cuida do cadastro de produtos.
# Aqui a gente usa um dicionário: cada produto tem um nome (chave)
# e um preço (valor). No final, mostramos tudo o que foi cadastrado.

def cadastrar_produtos():
    # dicionário vazio pra começar
    produtos = {}

    while True:
        # pergunta o nome do produto
        nome = input("Nome do produto (ou 'sair' para encerrar): ")
        # se digitar 'sair', encerra o cadastro
        if nome.lower() == "sair":
            break

        # aqui pedimos o preço. Usamos float porque pode ter centavos.
        preco = float(input("Preço: R$ "))

        # no dicionário, o nome é a chave e o preço é o valor
        produtos[nome] = preco

    print("\nProdutos cadastrados:")
    # .items() devolve chave e valor juntos (nome e preço)
    for nome, preco in produtos.items():
        # :.2f formata o número com duas casas decimais
        print(f"- {nome}: R$ {preco:.2f}")
