"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# for indice, nome in enumerate(lista):
#     print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

# FOR da tupla:
#         0
#         Maria
# FOR da tupla:
#         1
#         Helena
# FOR da tupla:
#         2
#         Luiz
# FOR da tupla:
#         3
#         João
