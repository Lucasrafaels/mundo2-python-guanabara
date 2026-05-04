#Programa que cria um jogo para o usuário adivinhar o número que o computador está "pensando"
from random import randint
computador = randint(0,10)
tentativas = 1
print ('Sou o seu computador e seu desafio é acertar o número que estou pensando de 0 a 10! \nVamos ver em quantas tentativas você consegue')
advinhacao_jogador = int(input('Digite o número que estou pensando: '))
while advinhacao_jogador != computador:
    if advinhacao_jogador < computador:
        advinhacao_jogador = int(input('O número que estou pensando é maior que esse, tente novamente: '))
    else:
        advinhacao_jogador = int(input('O número que estou pensando é menor que esse, tente novamente: '))
    tentativas += 1
print (f'Você acertou! com {tentativas} tentativas.')