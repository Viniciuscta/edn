def classificar_numeros():
    pares = 0
    impares = 0

    print("Digite números inteiros ou 'fim' para encerrar:")

    while True:
        entrada = input("Digite um número: ").strip()

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                impares += 1

        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

    print(f"Total de números inseridos: {pares + impares}")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

classificar_numeros()
