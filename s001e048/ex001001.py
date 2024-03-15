"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
print(string)
print(string[0])
print(string[4])
print(string[-5])
print(string[-1])

lista = []
print(lista, type(lista))

#        0    1      2                 3     4
#       -5   -4     -3                -2    -1
lista = [123, True, 'Taiane Barbosa',  1.2, []]
print(lista)
print(lista[2], type(lista[2]))
lista[-3] = 'Matheus Barbosa'
print(lista)
print(lista[2], type(lista[2]))
