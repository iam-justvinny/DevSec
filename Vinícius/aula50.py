'''
Exercicio
Exiba os índices da lista
0 Maria
1 Helena
3 Luiza
''' 
lista = ['Maria', 'Helena', 'Luiza']
lista.append('jõao')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
