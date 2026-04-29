#Novo programa para montar uma tabuada< dessa vez usando o 'for'
numero_tabuada = int(input('Digite um número para ver a sua tabuada: '))
for tabuada in range (0,11):
    print (f'{numero_tabuada}  X {tabuada:2} = {numero_tabuada*tabuada}')