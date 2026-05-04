from time import sleep
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
opcoes = 0
while opcoes != 5:
    print ('[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos números \n[ 5 ] Fechar programa')
    opcoes = int(input('Digite uma das opções acima: '))
    if opcoes == 1:
        soma = primeiro_numero + segundo_numero
        print (f'A soma dos números {primeiro_numero} e {segundo_numero} é igual: {soma} ')
    elif opcoes == 2:
        multiplicacao = primeiro_numero * segundo_numero
        print (f'A multiplicação entre o número {primeiro_numero} e o { segundo_numero} é igual: {multiplicacao}')
    elif opcoes == 3:
        if primeiro_numero > segundo_numero:
            condicao = 'O primeiro número é o maior'
        elif segundo_numero > primeiro_numero:
            condicao = 'O segundo número é o maior'
        else:
            condicao = 'Os dois números são iguais'
        print (condicao)
    elif opcoes == 4:
        print ('Informe os novos números')
        primeiro_numero = int(input('Digite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))
    elif opcoes == 5:
        print ('Finalizando o programa...')
    else:
        print ('Opção inválida, tente novamente')
        
    sleep (2)