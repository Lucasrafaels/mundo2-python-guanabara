#Programa para somar apenas os números pares que foram digitados
soma = 0
contador = 0
for c in range (1,7):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
     soma = soma + num
     contador = contador + 1
print (f'Você digitou {contador} números pares e a soma deles é igual a: {soma}')