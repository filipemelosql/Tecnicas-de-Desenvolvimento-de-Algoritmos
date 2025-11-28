# Programa: Cadastro simples de produtos
# Disciplina: Técnicas de Desenvolvimento de Algoritmos
# Conteúdo: Dicionários (dict)
# Autor: Filipe Melo

# Este programa cadastra produtos com nome e preço utilizando um dicionário.
# A chave do dicionário será o nome do produto e o valor será o preço.

# Criação do dicionário vazio
produtos = {}

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    # Condição de parada
    if nome.lower() == "sair":
        break

    # Leitura do preço do produto
    preco = float(input("Digite o preço do produto: R$ "))

    # Armazena no dicionário: chave = nome, valor = preço
    produtos[nome] = preco

print("\nProdutos cadastrados:")

# O método items() retorna pares (chave, valor) do dicionário
for nome, preco in produtos.items():
    print(f"- {nome}: R$ {preco:.2f}")

# Fim do programa
