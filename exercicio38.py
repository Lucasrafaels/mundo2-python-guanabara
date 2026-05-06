"""exercicio de comparação entre números inteiros"""

primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite um segundo número: '))
if primeiro_numero > segundo_numero:
    print(f'O número {primeiro_numero} é maior que {segundo_numero}')
elif segundo_numero > primeiro_numero:
    print(f'O número {segundo_numero} é maior que o {primeiro_numero}')
else:
    print ('Os dois números são iguais')