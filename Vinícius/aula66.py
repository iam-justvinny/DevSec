'''
Argumentos nomeados e não nomeados em funções python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebem apenas o argumento(valor)
'''


def soma(x, y): 
    #definição
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)

soma(1,2)
soma(y=2, x=1)