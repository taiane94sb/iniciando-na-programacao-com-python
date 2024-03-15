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
# print(next(iterador))  # T
# print(next(iterador))  # a
# print(next(iterador))  # i
# print(next(iterador))  # a
# print(next(iterador))  # n
# print(next(iterador))  # e

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
