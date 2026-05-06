'''Atualização do exercício 35 do mundo 1'''
print ('Digite três seguentos para verificar se formam um triângulo e se sim, qual tipo de trângulo!')
segmento1 = float(input('Digite o primeiro segmento: '))
segmento2 = float(input('Digite o segundo segmento: '))
segmento3 = float(input('Digite o terceiro segmento: '))
if segmento1 + segmento2 > segmento3 and segmento2 + segmento3 > segmento1 and segmento3 + segmento1 > segmento2:
    if segmento2 == segmento1 and segmento2 == segmento3:
        print ('Os segementos pode formar um triângulo de categoria: EQUILÁTERO')
    elif segmento1 != segmento2 and segmento2 != segmento3 and segmento1 != segmento3:
        print ('Os segementos pode formar um triângulo de categoria: ESCALENO')
    else:
        print ('Os segementos pode formar um triângulo de categoria: ISÓCELES')
else:
    print ('Os segmentos não podem formar um triângulo') 