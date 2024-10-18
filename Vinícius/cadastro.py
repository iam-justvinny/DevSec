
# Captura do número de usuários que serão cadastrados
n = int(input("Quantos usuários deseja cadastrar? "))

# Criação da matriz vazia
matriz = []

# Entrada de dados para cada usuário
for i in range(n):
    print(f"\n--- Cadastro do Usuário {i + 1} ---")
    nome = input("Nome: ")
    cpf = int(input("CPF: "))
    estado_civil = input("Estado Civil: ")
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
