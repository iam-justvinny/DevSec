"""
Dicionários em python (Tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor"
Chaves podem ser consideradas como o "Índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamosas chaves - {} - ou a classse dict para criar 
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
Pessoa = {
    'nome': 'vinicius',
    'sobrenome': 'Oliveira',
    'idade': 19,
    'Altura': 1.6,
    'endereços':[
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
        
    ]
}
"""
pessoa ={
    'nome': 'Vinicius',
    'sobrenome': 'Oliveira',
    'idade': 19,
        'Altura': 1.6,
    'endereços':[
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ],
}
print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])