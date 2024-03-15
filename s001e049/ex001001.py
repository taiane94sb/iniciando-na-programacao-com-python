"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
print(lista)  # [10, 20, 30, 40]
print()

print(lista[2])
lista[2] = 300
print(lista[2])  # 300
print(lista)  # [10, 20, 300, 40]
print()

print(lista[2])  # 300
del lista[2]
print(lista[2])  # 40
print(lista)  # [10, 20, 40]
print()

lista.append(50)
print(lista)  # [10, 20, 40, 50]
print()
lista.pop()
print(lista)  # [10, 20, 40]
print()
lista.append(60)
print(lista)  # [10, 20, 40, 60]
print()
lista.append(70)
print(lista)  # [10, 20, 40, 60, 70]
print()

ultimo_valor = lista.pop(3)  # 60
print(lista, 'Removido,', ultimo_valor)  # [10, 20, 40, 70] Removido, 60
