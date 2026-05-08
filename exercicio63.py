#Calcular a sequência de fibonacci usando o 'while'
print ('-'*25)
print ('Sequência de Fibonacci')
print ('-'*25)
quantidade_de_termos = int(input('Digite quantos termos você deseja ver: '))
print ('-'*35)
primerio_termo = 0
segundo_termo = 1
print (f'{primerio_termo} → {segundo_termo}', end = '')
contador_de_numerais = 3
while contador_de_numerais <= quantidade_de_termos:
    terceiro_termo = primerio_termo + segundo_termo
    print (f' → {terceiro_termo}', end = '')
    primerio_termo = segundo_termo
    segundo_termo = terceiro_termo
    contador_de_numerais += 1
print (' → Fim da progressão')