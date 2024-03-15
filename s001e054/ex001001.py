"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
print(lista)

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

# 0 Maria <class 'str'>
# 1 Helena <class 'str'>
# 2 Luiz <class 'str'>
# 3 João <class 'str'>
