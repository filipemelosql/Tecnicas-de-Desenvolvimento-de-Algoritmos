# Programa: Verificador de idade para entrada em eventos
# Disciplina: Técnicas de Desenvolvimento de Algoritmos
# Conteúdo: Estruturas Condicionais (if, elif, else)
# Autor: Filipe Melo

# Este programa simula um sistema simples de verificação de idade
# para entrada em um evento. A ideia é praticar o uso de estruturas
# condicionais em Python.

# Entrada de dados: o usuário informa a idade
idade = int(input("Digite sua idade: "))

# Verificação da idade usando if / elif / else
# Primeiro, validamos se a idade faz sentido
if idade < 0:
    print("Idade inválida. Por favor, tente novamente.")
# Menores de 18 anos não podem entrar
elif idade < 18:
    print("Entrada não permitida. Este evento é exclusivo para maiores de 18 anos.")
# De 18 até 59 anos: entrada normal
elif idade < 60:
    print("Entrada permitida! Bem-vindo(a) ao evento.")
# 60 anos ou mais: entrada com tratamento especial
else:
    print("Entrada permitida! Bem-vindo(a). Área especial disponível para idosos.")

# Fim do programa
