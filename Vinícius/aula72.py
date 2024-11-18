#Exercícios com funções

#Crie uma função que multiplica todos os argumentos 
#Não nomeados recebidos
#Retorne o total para uma variável e mostr o valor
#da variável


def mult(*args):
     total = 1
     for numeros in args:
         total *= numeros
     return total
mutliplicaco = mult()
print(mutliplicaco)


'''
Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
'''

def impar_ou_par(numero):
    if numero % 2 == 0:
        return f'0 número {numero} é par.'
    else:
        return f'O número {numero} é impar.'
    
    
resultado = impar_ou_par(7)
print(resultado)