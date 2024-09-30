print('Olá, seja bem vindo ao cálculo de imc.')
nome = input('Digite seu nome: ')
altura = float(input(f'Certo {nome}, agora digite sua altura: '))
peso = float(input(f'Digite seu peso: '))

imc = altura / peso ** 2

