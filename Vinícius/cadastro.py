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
    endereco = input("Endereço: ")
    telefone = int(input("Telefone: "))
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
        
        opcao = input("Opção: ")  # Entrada como string para evitar erro de conversão

        if opcao in ['1', '2', '3', '4']:
            if opcao == '1':
                estado_civil = "Solteiro(a)"
            elif opcao == '2':
                estado_civil = "Casado(a)"
            elif opcao == '3':
                estado_civil = "Divorciado(a)"
            elif opcao == '4':
                estado_civil = "Viúvo(a)"
            break  # Saída do laço se a opção for válida
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
