"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
print(nomes, type(nomes))  # ('Maria', 'Helena', 'Luiz') <class 'tuple'>
nomes = tuple(nomes)
print(nomes, type(nomes))  # ('Maria', 'Helena', 'Luiz') <class 'tuple'>
nomes = list(nomes)
print(nomes, type(nomes))  # ['Maria', 'Helena', 'Luiz'] <class 'list'>
print()

print(nomes[1])  # Helena
print(nomes[-1])  # Luiz
print(nomes)  # ['Maria', 'Helena', 'Luiz']
