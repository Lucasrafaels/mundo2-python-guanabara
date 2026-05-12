#Programa para jogar par ou ímpar contra o computador
from random import randint
while True:
    numero_jogador = int(input('Digite o número que você vai escolher: '))
    escolha_computador = randint(0,10)
    total = numero_jogador + escolha_computador
    escolha_jogador = ' '
    while escolha_jogador not in 'PI':
        escolha_jogador = input('Par ou Ímpar? [P/I]: ') .strip() .upper() [0]
    print (f'Você escolheu o número {numero_jogador} e o computador escolheu o número {escolha_computador}, o total é igual a: {total}')
    resultado = 'P' if total % 2 == 0 else 'I'
    if escolha_jogador == resultado:
        print('VOCÊ GANHOU!')
    else:
        print('VOCÊ PERDEU!')
        break
    print('Vamos jogar novamente...')