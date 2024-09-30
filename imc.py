print('Olá, seja bem vindo ao cálculo de imc.')
nome = input('Digite seu nome: ')
altura = float(input(f'Certo {nome}, agora digite sua altura: '))
peso = float(input(f'Digite seu peso: '))

imc = altura / peso ** 2

if imc < 18.5:
    print(f'{nome}, seu imc é: {imc}, você está abaixo do peeso')

elif imc >= 18.5 <= 24.9:
    print(f'{nome}, seu imc é:  {imc}, você está no peso normal.')

elif imc >= 25.0 <= 29.9:
    print(f'{nome}, seu imc é: {imc}, você está acima do peso.')

elif imc >= 30.0 <= 34.9:
    print(f'{nome}, seu imc é: {imc}, você está com obesidade nível 1.')

elif imc >= 35.0 <= 39.9:
    print(f'{nome}, seu imc é: {imc}, você está com obesidade nível 2.')

else:
    print(f'{nome}, seu imc é: {imc}, você está com obesidade nível 2')