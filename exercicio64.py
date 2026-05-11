#Programa para calcular os números digitados usando o 'while'
numero_digitado = int(input('Digite um número [digite "999" para parar]: '))
somatoria = 0
quantidade_numeros = 0 
while numero_digitado != 999:
    somatoria += numero_digitado
    numero_digitado = int(input('Digite um número [digite "999" para parar]: '))
    quantidade_numeros += 1
print (f'Vocẽ digitou {quantidade_numeros} números, e a soma de todos os números digitados é igual a: {somatoria}')