"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# for indice, nome in enumerate(lista):
#     print(indice, nome, lista[indice])

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

# 0 Maria
# 1 Helena
# 2 Luiz
# 3 João
