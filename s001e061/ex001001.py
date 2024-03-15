"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

print(salas)  # [['Maria', 'Helena'], ['Elaine'], ['Luiz', 'João', 'Eduarda']]
print()

print(salas[0])  # ['Maria', 'Helena']
print(salas[1])  # ['Elaine']
print(salas[2])  # ['Luiz', 'João', 'Eduarda']
print()

print(salas[0][0])  # Maria
print(salas[0][1])  # Helena
print()

print(salas[1][0])  # Elaine
print()

print(salas[2][0])  # Luiz
print(salas[2][1])  # João
print(salas[2][2])  # Eduarda
print()

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
