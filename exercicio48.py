#Programa que soma todos os números múltiplos de 3 
soma = 0
listar = 0
for contador in range  (1,501):
    if contador % 3 == 0:
        soma = soma + contador
        listar = listar + 1
print (f'A soma de todos os {listar} números múltiplos de 3 (de 0 até 500) é igual a: {soma}')