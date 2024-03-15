"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
print(lista)  # [10, 20, 30, 40]
lista.append('Taiane')
print(lista)  # [10, 20, 30, 40, 'Taiane']
nome = lista.pop()
print(lista)  # [10, 20, 30, 40]
lista.append(1234)
print(lista)  # [10, 20, 30, 40, 1234]
del lista[-1]
print(lista)  # [10, 20, 30, 40,]
lista.clear()
print(lista)  # []
print()

lista = [10, 20, 30, 40]
print(lista)  # [10, 20, 30, 40]
lista.insert(100, 5)
print(lista)  # [10, 20, 30, 40, 5]
print(lista[4])  # 5
print(lista)  # [10, 20, 30, 40, 5]
