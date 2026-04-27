'''Jogo de 'pedra, papel ou tesoura' '''
from random import randint
opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)
print ('[ 0 ] Pedra ')
print ('[ 1 ] Papel')
print ('[ 2 ] Tesoura')
escolha_jogador = int(input('Escolha uma das opções acima para jogar: '))
print (f'O computador escolheu {opcoes[computador]}')
print (f'O jogador escolheu {opcoes[escolha_jogador]}')
if computador == 0:
    if escolha_jogador == 0:
        print('EMPATE, ambos escolheram a mesma opção!')
    elif escolha_jogador == 1:
        print ('O jogador ganhou! Papel vence pedra.')
    elif escolha_jogador == 2:
        print ('O computador ganhou! Pedra vence tesoura.')
    else:
        print ('Opção inválida')
elif computador == 1:
    if escolha_jogador == 0:
        print('O computador ganhou! Papel vence pedra.')
    elif escolha_jogador == 1:
        print ('EMPATE, ambos escolheram a mesma opção!')
    elif escolha_jogador == 2:
        print ('O jogador ganhou! Tesoura vence papel.')
    else:
        print ('Opção inválida')
elif computador == 2:
    if escolha_jogador == 0:
        print('O jogador venceu! Pedra vence tesoura')
    elif escolha_jogador == 1:
        print ('O computador venceu! Tesoura vence papel.')
    elif escolha_jogador == 2:
        print ('EMPATE, ambos escolheram a mesma opção!')
    else:
        print ('Opção inválida')