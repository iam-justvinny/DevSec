nome = input('Olá, tudo bem? Iniciaremos nossa pesquisa de satisfação, me diga seu nome: ')
idade = input(f'Certo {nome}, quantos anos você tem? ')

print('Ótimo.')

print("\nEscolha uma das opções de cursos:")
print("1. CIÊNCIA DA COMPUTAÇÃO (CCP)")
print("2. ANÁLISE E DESENVOLVIMENTO DE SISTEMAS (ADS)")

opcao = input("Digite o número da sua escolha: ")

if opcao == '1':
    print(f"Você escolheu CCP.")
    gosta = input(f'{nome}, você gosta desse curso? (SIM/NÃO): ').upper()
elif opcao == '2':
    print(f"Você escolheu ADS.")
    gosta = input(f'{nome}, você gosta desse curso? (SIM/NÃO): ').upper()
else:
    gosta = input("Você gosta desse curso? (SIM/NÃO): ").upper()

if gosta == "SIM":
    print('Que bom que você gosta!')
    nota = int(input('De 0 a 10, qual seria sua nota para o curso? '))
    if 0 <= nota <= 5:
        print("Ok, obrigado.")
    elif 6 <= nota <= 10:
        print("Uau, que incrível!")
    else:
        print("Nota inválida. Deve ser entre 0 e 10.")
elif gosta == "NÃO":
    print('Que pena!')
    nota = int(input('De 0 a 10, qual seria sua nota? '))
    if 0 <= nota <= 5:
        print("Ok, obrigado.")
    elif 6 <= nota <= 10:
        print("Uau, que incrível!")
    else:
        print("Nota inválida. Deve ser entre 0 e 10.")
else:
    print("Resposta coletada. Fim da pesquisa.")
