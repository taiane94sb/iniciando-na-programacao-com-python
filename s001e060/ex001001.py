"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
print(frase)
lista_frases_cruas = frase.split(',')
print(lista_frases_cruas)  # ['   Olha só que   ', ' coisa interessante          ']
print()

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)  # ['   Olha só que   ', ' coisa interessante          ']
print(lista_frases)
print()

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)  # Olha só que, coisa interessante
