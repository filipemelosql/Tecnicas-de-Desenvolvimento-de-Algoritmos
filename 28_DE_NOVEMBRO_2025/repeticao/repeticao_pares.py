# Programa: Contador de números pares de 1 a 100
# Disciplina: Técnicas de Desenvolvimento de Algoritmos
# Conteúdo: Estruturas de Repetição (for e while)
# Autor: Filipe Melo

# Este programa exibe apenas os números pares de 1 a 100,
# primeiro utilizando o laço for e depois utilizando o laço while.

print("Números pares de 1 a 100 (usando FOR):")

# Uso do laço FOR
# range(1, 101) gera números de 1 até 100 (o 101 não entra)
for numero in range(1, 101):
    # Se o resto da divisão por 2 for zero, o número é par
    if numero % 2 == 0:
        print(numero)

print("\nNúmeros pares de 1 a 100 (usando WHILE):")

# Uso do laço WHILE
num = 1  # inicializa o contador

# Enquanto num for menor ou igual a 100, o laço continua
while num <= 100:
    if num % 2 == 0:
        print(num)
    # Incremento do contador para evitar loop infinito
    num += 1

# Fim do programa
