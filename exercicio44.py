'''`Programa de cálculo de desconto de acordo com a forma de pagamento'''
valor_produto = float(input('Digite o valor do produto escolhido: '))
print ('Qual será a forma de pagamento?')
print ('[ 1 ] No dinheiro ou no pix')
print ('[ 2 ] À vista no cartão')
print ('[ 3 ] 2 vezes no cartão')
print ('[ 4 ] 3 vezes (Ou mais) no cartão')
opcao_compra = int(input('Digite uma das opções acima: '))
if opcao_compra == 1:
    valor_final = valor_produto - (valor_produto * (10/100))
elif opcao_compra == 2:
    valor_final = valor_produto - (valor_produto * (5/100))
elif opcao_compra == 3:
    valor_final = valor_produto 
elif opcao_compra == 4:
    valor_final = valor_produto + (valor_produto * (20/100))
else:
    print ('Opção inválida, tente novamente')

print (f'O valor do seu produto após a escolha do método de pagamento será de: {valor_final}')