'''
closure e funções que retornam outras funções
'''
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bomdia = criar_saudacao('bom dia')
falar_boanoite = criar_saudacao('Boa noite')


for nome in ['vinicius', 'Claire', 'Jordan']:
    print(falar_bomdia (nome))
    print(falar_boanoite (nome))
