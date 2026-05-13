#Programa simulador de caixa eletrônico
print ('-'*20)
print ('Sistema bancário')
print ('-'*20)
valor_sacado = int(input('Digite o valor que deseja sacar: R$'))
total = valor_sacado
valor_da_nota = 50
total_de_notas = 0
while True:
    if total >= valor_da_nota:
        total -= valor_da_nota
        total_de_notas += 1
    else:
        if total_de_notas > 0:
            print (f'Total de {total_de_notas} notas de R${valor_da_nota}')
        if valor_da_nota == 50:
            valor_da_nota = 20
        elif valor_da_nota == 20:
            valor_da_nota = 10
        elif valor_da_nota == 10: 
            valor_da_nota = 1
        total_de_notas = 0
        if total == 0:
            break
print('-' * 20)
print('Saque finalizado com sucesso.')