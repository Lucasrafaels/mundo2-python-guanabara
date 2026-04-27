'''Programa para definir categoria por idade'''
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite seu ano de nascimento para definir sua categoria: '))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print (f'Você tem {idade} anos e a sua categoria é: MIRIM') 
elif idade <= 14:
    print (f'Você tem {idade} anos e a sua categoria é: INFANTIL') 
elif idade <= 19:
    print (f'Você tem {idade} anos e a sua categoria é: JUNIOR') 
elif idade <= 25:
    print (f'Você tem {idade} anos e a sua categoria é: SÊNIOR') 
else:
    print (f'Você tem {idade} anos e a sua categoria é: MASTER') 