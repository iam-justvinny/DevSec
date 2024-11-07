print('-' * 100)
print('Olá! Seja bem-vindo(a) ao cadastro de currículo.')
print('-' * 100)

print('Digite seu nome\n')
nome = input('nome: ')
# Captura do número de usuários que serão cadastrados
n = int(input(f"{nome} Quantos usuários deseja cadastrar? "))

# Criação da matriz vazia
matriz = []

# Entrada de dados para cada usuário
for i in range(n):
    print(f"\n{'-' * 40} Cadastro do Usuário {i + 1} {'-' * 40}")
    nome = input("Nome: ")
    cpf = input("CPF: ")  # CPF como string para preservar formatação
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")  # Telefone como string para preservar formato

    # Laço para garantir que o e-mail tenha um domínio válido
    while True:
        email = input("E-mail: ")
        if (email.endswith("@gmail.com") or
            email.endswith("@hotmail.com") or
            email.endswith("@yahoo.com") or
            email.endswith("@outlook.com")):
            break
        else:
            print("E-mail inválido! Use um e-mail com @gmail.com, @hotmail.com, @yahoo.com ou @outlook.com.")

    # Laço para garantir a escolha de uma opção válida de estado civil
    while True:
        print("\nEscolha o estado civil:")
        print("[1] Solteiro(a)")
        print("[2] Casado(a)")
        print("[3] Divorciado(a)")
        print("[4] Viúvo(a)")

        opcao = input("Opção: ")  # Entrada como string

        if opcao in ['1', '2', '3', '4']:
            estado_civil = {
                '1': "Solteiro(a)",
                '2': "Casado(a)",
                '3': "Divorciado(a)",
                '4': "Viúvo(a)"}[opcao]
            break
        else:
            print("Opção inválida! Tente novamente.")

    resumo_curriculo = input("Resumo do Currículo: ")

    # Adiciona os dados do usuário como uma nova linha na matriz
    matriz.append([
        nome, cpf, endereco, telefone, email, estado_civil, resumo_curriculo])

# Exibe a matriz com os dados cadastrados
print("\n" + "=" * 50 + " Dados Cadastrados " + "=" * 50)
for i in range(n):
    print(f"\n{'-' * 40} Usuário {i + 1} {'-' * 40}")
    print(f"{'Nome:':<15} {matriz[i][0]}")
    print(f"{'CPF:':<15} {matriz[i][1]}")
    print(f"{'Endereço:':<15} {matriz[i][2]}")
    print(f"{'Telefone:':<15} {matriz[i][3]}")
    print(f"{'E-mail:':<15} {matriz[i][4]}")
    print(f"{'Estado Civil:':<15} {matriz[i][5]}")
    print(f"{'Resumo:':<15} {matriz[i][6]}")
print("=" * 100)

print(f'Parabens!{nome} você terminou seu trabalho, muito bem!')