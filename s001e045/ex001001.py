"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Taiane'  # iterável
print(texto)  # Taiane
iterador = iter(texto)  # iterator -> __iter__()
print(iterador.__next__())  # T
print(iterador.__next__())  # a
print(iterador.__next__())  # i
print(iterador.__next__())  # a
print(iterador.__next__())  # n
print(iterador.__next__())  # e

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break
