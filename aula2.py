# Algoritmo que calcula a média de alunos informada pelo usuário
# Inicializa com a quantidade de alunos informada pelo usuário
cont = 1
QTDALUNOS = int(input(f"Digite a quantidade de alunos: "))

# Loop para ler as notas da quantidade de alunos informada pelo usuário
while cont <= QTDALUNOS:
    aluno = input(f"Digite o nome do aluno: ")
    print(f"Vamos calcular a nota do aluno {aluno}")
    nota1 = float(input(f"Digite a nota 01 do aluno: "))
    nota2 = float(input(f"Digite a nota 02 do aluno: "))
    nota3 = float(input(f"Digite a nota 03 do aluno: "))
    # Calcula a média das notas do aluno
    media = (nota1 + nota2 + nota3) / 3

    # Exibe a média do aluno e se está aprovado ou reprovado
    print(f"A média do aluno nº {cont} {aluno} é: {media:.2f}")
    if media >= 6:
        print("O aluno está aprovado!")
    else:
        print("O aluno está reprovado!")

    cont += 1
