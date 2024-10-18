print('-' * 100)
print('Olá, seja bem vindo ao cadastro de currículo!')
print('-' * 100)
nome = input('Para começar digite seu nome\nNome:  ')
cpf = int(input(f'{nome}, digite seu cpf\nCPF: '))
estado_civil = False
while estado_civil == True:
    estado_civil = int(input(f'\n{nome}, qual seu estado civil? \n[1]Solteiro(a) \n[2]Casado(a) \n[3]Divorciado(a) \n[4]Viúvo(a)\nEstado civil: '))
    if '1' or '2' or '3' or '4' not in estado_civil:
        estado_civil = False
    else:
        estado_civil = True
    break
print("acabou")
