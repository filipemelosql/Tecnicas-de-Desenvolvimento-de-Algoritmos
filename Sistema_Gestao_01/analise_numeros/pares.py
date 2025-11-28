# Esse arquivo é responsável pela parte de números pares.
# Aqui a missão é mostrar os números pares de 1 até 100,
# primeiro usando for e depois usando while.

def mostrar_pares():
    print("\nPares usando FOR:")
    # range(1, 101) vai de 1 até 100 (o 101 não entra)
    for n in range(1, 101):
        # se o resto da divisão por 2 for zero, o número é par
        if n % 2 == 0:
            print(n)

    print("\nPares usando WHILE:")
    n = 1  # começamos o contador em 1

    # enquanto n for menor ou igual a 100, o while continua rodando
    while n <= 100:
        if n % 2 == 0:
            print(n)
        # muito importante: sempre incrementar o n,
        # senão o while fica preso pra sempre (loop infinito)
        n += 1
