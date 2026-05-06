#Program para saber a quantidade de maiores e menores de idade
from datetime import date
ano_atual = date.today() .year
maiores_de_idade = 0
menores_de_idade = 0
for pessoas in range (1,8):
    ano_de_nascimento = int(input('Digite o primeiro ano de nascimento: '))
    idade = ano_atual - ano_de_nascimento
    if idade >= 18:
        maiores_de_idade = maiores_de_idade + 1
    else:
        menores_de_idade = menores_de_idade + 1
        
print (f'A quantidade de maiores de idade é {maiores_de_idade} e a quantidade de menores de idade é {menores_de_idade}')

