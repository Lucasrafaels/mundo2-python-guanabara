#Sistema que armazena informações de uma compra
print ('-'*20)
print ('Digite os produtos que você pegou para poder comprar')
print ('-'*20)
soma_dos_produtos = 0
mais_de_1000 = 0
menor_preço = 0
contador = 0
nome_mais_barato = ' '
while True:
    nome_produto = input('Digite o nome do produto que escolheu:').strip()
    preco_produto = float(input('Digite o preço desse produto: R$'))
    contador += 1
    continuar = ' '
    if contador == 1 or preco_produto < menor_preço:
        menor_preço = preco_produto
        nome_mais_barato = nome_produto
    while continuar not in 'SN':
        continuar = input('Deseja continuar[S/N]? ').strip() .upper() [0]
    soma_dos_produtos += preco_produto
    if preco_produto >= 1000:
        mais_de_1000 += 1
    if continuar == 'N':
        break
print ('-'*30)
print (f'O total das compras foi de R${soma_dos_produtos:.2f}')
print(f'A quantidade produtos que custaram mais de R$1000 foi de: {mais_de_1000}')
print (f'O produto com o menor valor foi {nome_mais_barato} e custou R${menor_preço:.2f}')