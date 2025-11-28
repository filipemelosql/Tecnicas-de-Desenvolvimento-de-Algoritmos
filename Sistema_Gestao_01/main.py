# Esse é o arquivo principal do projeto.
# Pensa nele como o "menu inicial" do sistema.
# É aqui que o usuário escolhe o que quer fazer,
# e daqui a gente chama as funções que estão nos outros arquivos.

# Importando as funções dos outros módulos (arquivos)
# Cada linha dessas aponta pra uma "parte" do sistema.
from verificacao_idade.idade import verificar_idade
from analise_numeros.pares import mostrar_pares
from cadastro_alunos.alunos import cadastrar_alunos
from cadastro_produtos.produtos import cadastrar_produtos

def menu():
    # esse while True mantém o sistema rodando até o usuário querer sair
    while True:
        print("\n=== SISTEMA DE GESTÃO BÁSICA ===")
        print("1 - Verificação de Idade")
        print("2 - Análise de Números Pares")
        print("3 - Cadastro de Alunos")
        print("4 - Cadastro de Produtos")
        print("0 - Sair")

        # aqui a gente lê a opção que o usuário digitou
        opcao = input("Escolha uma opção: ")

        # e aqui começam os ifs pra saber o que fazer com essa opção
        if opcao == "1":
            # se a pessoa escolheu 1, chamamos a função que trata de idade
            verificar_idade()
        elif opcao == "2":
            # se escolheu 2, chama a parte que mostra números pares
            mostrar_pares()
        elif opcao == "3":
            # se escolheu 3, entra no cadastro de alunos
            cadastrar_alunos()
        elif opcao == "4":
            # se escolheu 4, entra no cadastro de produtos
            cadastrar_produtos()
        elif opcao == "0":
            # opção 0 é pra encerrar o programa
            print("Encerrando o sistema... Valeu!")
            break
        else:
            # qualquer coisa diferente de 0 a 4 é inválida
            print("Opção inválida. Digita direitinho aí e tenta de novo.")

# Essa linha aqui é o ponto de partida.
# Quando o arquivo main.py for executado, ele começa chamando o menu().
if __name__ == "__main__":
    menu()
