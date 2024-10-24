'''
def saudação():
    print('Sejam bem vindos')

saudação()
'''

#---------------------------------------------

'''
def primeirograu(a,b,x):
    return a+(b*x)

resultado = primeirograu(3,2,6)
print(resultado)
'''

#---------------------------------------------

'''
def cadastro(): #define a função
    nome=[] #armazena os nomes informados
    for i in range(5): #define a quantidade de vezes que será executado
        namecard = input(f'Digite o nome {i+1}:') #solicita ao usuário que insira os nomes
        nome.append(namecard) #adiciona o nome inserido a lista 'nome=[]' usando o método '.append()', que coloca o valor inserido no final da lista
        print(nome) #cada vez que um nome for inserido será mostrado a lista atualizada ao usuário
        
cadastro() #executa a função, exibindo os nomes coletados em cada processo
'''

#---------------------------------------------

# A função 'lambda' recebe um argumento 'x' e retorna o quadrado desse valor. Não precisa ser definida com 'def'

'''
quadrado = lambda x: x*x
print(quadrado(2))
'''

'''
quadrado = lambda x,y: x*y
print(quadrado(2,6))
'''

#EXERCÍCIO 1

'''
def multiplica_por_dois(numero):
    return numero * 2
resultato = multiplica_por_dois(7)
print(resultato)

multiplica_por_dois = lambda x,y: x*y
print(multiplica_por_dois(2,7))
'''

#--------------------------------------------

#EXERCÍCIO 2

'''
def conta_vogais(texto):
    vogais = 'a, e, i, o, u, A, E, I, O, U'
    contador = 0
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

resultado = conta_vogais('Programação em Python')
print(f'O número de vogais é: {resultado}')
'''

#--------------------------------------------

#EXERCÍCIO 3

'''
def verificador_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input('Digite um ano: '))

if verificador_ano_bissexto(ano):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
'''

#---------------------------------------------

#EXERCÍCIO 4

'''
def conta_vogais(texto):
    vogais = 'a, e, i, o, u, A, E, I, O, U'
    contador = 0
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

texto = input('Digite a frase: ')

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")
'''

#---------------------------------------------

#EXERCÍCIO 5

def elementos_comuns(lista1, lista2):
    lista1 = list(map(int, lista1.split()))
    lista2 = list(map(int, lista2.split()))
    
    comuns = list(set(lista1) & set(lista2))
    
    return comuns

lista1 = input('Digite os números da primeira lista, separados por espaço: ')
lista2 = input('Digite os números da segunda lista, separados por espaço: ')

resultado = elementos_comuns(lista1, lista2)
print('Elementos comuns: ', resultado)