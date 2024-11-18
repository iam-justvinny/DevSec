'''
valores padrão para parâmetros
Ao definir uma fução, os parâmetros podem
ter valores padrão. Caso ovalor não seja
enviado parar o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
'''

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(9, 3)
soma(200, 100)
soma(20, 10, 0)