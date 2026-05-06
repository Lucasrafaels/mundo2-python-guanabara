'''Programa para ver situação do alistamento militar obrigatório'''
from datetime import date
data_atual = date.today().year
ano_de_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = data_atual - ano_de_nascimento
if idade > 18:
    saldo = idade - 18
    print ('A sua idade de alistamento já passou!')
elif idade < 18:
    saldo = 18 - idade
    print (f'Ainda faltam {saldo} anos para o seu alistamento')
else:
    print ('Você deve se alistar imediatamente')