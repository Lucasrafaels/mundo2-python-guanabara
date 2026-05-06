#Programa para calcular fatorial usando o 'while'
numero_digitado = int(input('Digite um número para calcular o seu fatorial: '))
inicio_do_fatorial = numero_digitado
fator_de_multipicacao = 1
print (f'O resultado de {numero_digitado} fatorial é igual a: ', end = '')
while inicio_do_fatorial > 0:
    print (f'{inicio_do_fatorial}', end = ' ')
    print ('x' if inicio_do_fatorial >1 else '=', end = ' ')
    fator_de_multipicacao *= inicio_do_fatorial
    inicio_do_fatorial -= 1
print (fator_de_multipicacao)
print ()