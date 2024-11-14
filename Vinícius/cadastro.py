print('-' * 100)
print('Olá, seja bem vindo ao cadastro de currículo!')
print('-' * 100)
nome = input('Para começar digite seu nome\nNome:  ')
cpf = int(input(f'{nome}, digite seu cpf\nCPF: '))

while True:
    estado_civil = input(f'\n{nome}, qual seu estado civil? \n[1]Solteiro(a) \n[2]Casado(a) \n[3]Divorciado(a)\n[4]Viúvo(a)\nEstado civil: ')
    if estado_civil == 1:
        estado_civil = 'Solteiro(a)'
        break
    elif estado_civil == 2:
        estado_civil = 'Casado(a)'
        break
    elif estado_civil == 3:
        estado_civil = 'Divorciado(a)'
        break
    elif estado_civil == 4:
        estado_civil = 'Viúvo(a)'
        break
    else:
        print('Opção incorreta')
print("acabou")
