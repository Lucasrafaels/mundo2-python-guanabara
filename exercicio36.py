"""programa para liberar empréstimo para a compra de uma casa""" 

valor_casa = float(input('Digite o valor da casa que você que comprar: '))
salario_comprador = float(input('Digite o seu salário: '))
anos_de_pagamento = int(input('Digite em quantos anos pretende pagar:'))
prestacao_mensal = valor_casa / (anos_de_pagamento * 12)
limite = salario_comprador * (30/100)
if limite >= prestacao_mensal:
    print ('O empréstimo foi concedidio')
else:
    print ('O seu empréstimo não foi aprovado')