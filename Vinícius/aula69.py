'''
Escopo de funções em Python
Escopo signifina o local onde aquele códigopode atingir.
Existe o escopo global e local.
O escopo global e o escopo onde todo o código é alcançavel.
o escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra global faz uma variável do escopo externo
ser a mesma no escopo interno.
'''
x = 1




def escopo():
    global x
    x = 10
    
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)