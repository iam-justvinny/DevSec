'''
Métodos úteis dos dicionários em Python
Len - quantas chaves
Keys  - iterável com as chaves
values = iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona uma cópia rasa(shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada(del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''
pessoa = {
    'nome': 'Vinicius Oliveira',
    'sobrenome': 'Silva',
}
print(pessoa.__len__())