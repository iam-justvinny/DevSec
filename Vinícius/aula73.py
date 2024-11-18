'''
Higher Order Functions
Funções de primeira classe
'''

def saudadao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)

v = executa(saudadao, 'bom dia', 'vinicius')
print(v)
