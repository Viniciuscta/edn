def registrar_notas():
    notas = []

    print("Digite as notas dos alunos (0 a 10) ou 'fim' para encerrar:")

    while True:
        entrada = input("Digite uma nota: ").strip().lower()

        if entrada == 'fim':
            break

        try:
            nota = float(entrada)

            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"Nota {nota} registrada com sucesso!")
            else:
                print("Erro: Nota inválida! Digite uma nota entre 0 e 10.")

        except ValueError:
            print("Erro: Entrada inválida! Digite um número ou 'fim' para encerrar.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Total de notas registradas: {len(notas)}")
        print(f"Notas: {notas}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("\nNenhuma nota foi registrada.")

registrar_notas()
