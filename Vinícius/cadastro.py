print('-' * 100)
print('Olá! Seja bem vindo(a) ao cadastro de currículo.')
print('-' * 100)
# Captura do número de usuários que serão cadastrados
n = int(input("Quantos usuários deseja cadastrar? "))

# Criação da matriz vazia
matriz = []

# Entrada de dados para cada usuário
for i in range(n):
    print(f"\n--- Cadastro do Usuário {i + 1} ---")
    nome = input("Nome: ")
    cpf = int(input("CPF: "))
    # Laço para garantir a escolha de uma opção válida de estado civil
    while True:
        print("\nEscolha o estado civil:")
        print("[1] Solteiro")
        print("[2] Casado")
        print("[3] Divorciado")
        print("[4] Viúvo")
        opcao = int(input("Opção: "))

        # Verifica se a opção é válida e armazena o estado civil correspondente
        if opcao == '1':
            estado_civil = "Solteiro(a)"
            break
        elif opcao == '2':
            estado_civil = "Casado(a)"
            break
        elif opcao == '3':
            estado_civil = "Divorciado(a)"
            break
        elif opcao == '4':
            estado_civil = "Viúvo(a)"
            break
        else:
            print("Opção inválida! Tente novamente.")

    resumo_curriculo = input("Resumo do Currículo: ")

    # Adiciona os dados do usuário como uma nova linha na matriz
    matriz.append([nome, cpf, estado_civil, resumo_curriculo])

# Exibe a matriz com os dados cadastrados
print("\n=== Dados Cadastrados ===")
for i in range(n):
    print(f"\nUsuário {i + 1}:")
    print(f"Nome: {matriz[i][0]}")
    print(f"CPF: {matriz[i][1]}")
    print(f"Estado Civil: {matriz[i][2]}")
    print(f"Resumo do Currículo: {matriz[i][3]}")
