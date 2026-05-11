#Programa utilizando o 'while' para informar a média dos números digitados e qual foi o maior e o menor
soma_numeros = quantidade_numeros = media = maior_numero = menor_numero = 0
continuar = 'S'
while continuar == 'S':
    numero_digitado = int(input('Digite um número: '))
    soma_numeros += numero_digitado
    quantidade_numeros += 1
    continuar = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if quantidade_numeros == 1:
        maior_numero = menor_numero = numero_digitado
    else:
        if numero_digitado > maior_numero:
            maior_numero = numero_digitado
        if numero_digitado < menor_numero:
            menor_numero = numero_digitado
media = soma_numeros / quantidade_numeros
print (f'Você digitou {quantidade_numeros} números e a média total dos númerops digitador é igual a: {media:.2f}')
print (f'O maior número digitado foi o: {maior_numero} e o menor número digitado foi: {menor_numero}')