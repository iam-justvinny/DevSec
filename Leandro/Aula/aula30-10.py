#EXERCÍCIO 1

def multiplica_por_dois(numero):
    return numero * 2
resultato = multiplica_por_dois(7)
print(resultato)

#-----------------------------------------------------------------
#EXERCÍCIO 2

def conta_vogais(texto):
    vogais = 'a, e, i, o, u, A, E, I, O, U'
    contador = 0
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

texto = input('Digite a frase: ')

resultado = conta_vogais(texto)
print(f"O número de vogais na frase '{texto}' é: {resultado}")

#-----------------------------------------------------------------
#EXERCÍCIO 3

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