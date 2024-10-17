nomes = []
for i in range(5):
    nome = input(f'digite o nome {i+1}:')
    nomes.append(nome)
print('\nOs nomes inseridos foram: ')
for i, nome in enumerate(nomes, start = 1):
    print(f'{i} - {nome}')