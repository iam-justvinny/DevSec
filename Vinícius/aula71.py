'''
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''
# Lembre-se de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
        
    return total


soma1_2_3 = soma(1, 2, 3)
print(soma1_2_3)

