"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 11
print(condicao)
print()

variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)
print()

digito = 9
print(digito)
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
print()

print('Valor' if False else 'Outro valor' if False else 'Fim')
