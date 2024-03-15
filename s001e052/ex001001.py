"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Taiane', 'Matheus', 1, True, 1.2]
lista_b = lista_a
print(lista_a)  # ['Taiane', 'Matheus', 1, True, 1.2]
print(lista_b)  # ['Taiane', 'Matheus', 1, True, 1.2]

lista_a[0] = 'Qualquer coisa'
print(lista_a)  # ['Qualquer coisa', 'Matheus', 1, True, 1.2]
print(lista_b)  # ['Qualquer coisa', 'Matheus', 1, True, 1.2]
