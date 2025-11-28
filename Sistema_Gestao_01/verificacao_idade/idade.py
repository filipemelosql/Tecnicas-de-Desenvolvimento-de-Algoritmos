# Esse arquivo aqui cuida só da parte de idade.
# A ideia é: perguntar a idade da pessoa e liberar (ou não) o acesso,
# usando if / elif / else de um jeito bem simples.

def verificar_idade():
    # pede a idade pro usuário
    idade = int(input("Digite sua idade: "))

    # primeira checagem: idade negativa não faz sentido
    if idade < 0:
        print("Idade inválida, tenta de novo depois.")
    # aqui é menor de idade, então a ideia é bloquear
    elif idade < 18:
        print("Acesso negado: esse sistema é só para maiores de 18.")
    # entre 18 e 59 anos: vida normal, acesso liberado
    elif idade < 60:
        print("Acesso liberado: bem-vindo(a), acesso padrão.")
    # 60 ou mais: honra aos idosos, acesso especial
    else:
        print("Acesso liberado: você tem acesso especial para idosos.")
