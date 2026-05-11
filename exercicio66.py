#Programa para calcular a soma de todos os números digitados usando o 'while' e o 'break'
quantidade_numeros = 0
somatorio = 0
while True:
       numero_digitado = int(input('Digite um número [Digite "999" para parar]: '))
       if numero_digitado == 999:
              break
       quantidade_numeros += 1
       somatorio += numero_digitado
print (f'você digitou um total de {quantidade_numeros} números e a soma entre eles é igual a: {somatorio}')