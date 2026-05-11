#Programa atualizado para calcular a tabuada de um número digitado
while True:
    numero_digitado = int(input('Digite um número [POSITIVO] para ver a sua tabuada: '))
    if numero_digitado < 0:
        break
    print ('-' * 30)
    for tabuada in range (1,11):
        print (f'{numero_digitado}  X {tabuada:2} = {numero_digitado * tabuada}')
    print ('-' * 30)
print ('Fim do programa')