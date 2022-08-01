import functools

lista = [1, 6, 8, 7, 9, 3]
listaF = filter(lambda x: (x % 2 != 0), lista)
NumeroImpares = list(listaF)
print('Lista de numero impares: ', NumeroImpares)

def suma(a, b):
    return a + b

SumaNumero = functools.reduce(lambda a, b: a + b, NumeroImpares)
print('Suma de impares es: ', SumaNumero)
