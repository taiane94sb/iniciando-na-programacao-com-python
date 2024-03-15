nome = 'Taiane Barbosa'
altura = 1.66
peso = 54
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Taiane Barbosa tem 1.66 de altura,
# pesa 54 quilos e seu imc é
# 19.60
