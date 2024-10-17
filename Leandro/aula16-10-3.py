#criando uma matriz a partir de entradas do usuário
linhas=int(input('Digite o número de linhas: '))
colunas=int(input('Digite o número de colunas: '))
matriz=[]
#laço de repetição - preenchimento da matriz
# Adotaremos i para linha e j para coluna
for i in range(linhas):
    linha=[]
    for j in range(colunas):
        valor=int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)
for linha in matriz:
    print(linha)