"""Conversor de bases númericas"""

numero_escolhido = int(input('Digite um número para ser convertido para outra base númerica: '))
print ('Digite [ 1 ] para Binário')
print ('Digite [ 2 ] para Octal')
print ('Digite [ 3 ] para Hexadecimal')
opcao_de_escolha = int(input('Digite a Sua opão de escolha: '))
if opcao_de_escolha == 1:
    print (f'O número {numero_escolhido} em binário é igual a:{bin(numero_escolhido)[2:]}')
elif opcao_de_escolha == 2:
    print (f'O número {numero_escolhido} em binário é igual a:{oct(numero_escolhido)[2:]}')
elif opcao_de_escolha == 3:
    print (f'O número {numero_escolhido} em binário é igual a:{hex(numero_escolhido)[2:]}')
else:
    print('Você não digitou nenhuma das opções')