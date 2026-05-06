#Programa para calcular os 10 primeiros termos de uma progressão aritmética
termo_pa = int(input('Digite o primeiro termo da P.A: '))
razao_pa = int(input('Digite a razão da P.A: '))
decimo_termo = termo_pa + (11-1) * razao_pa
for progressao in range (termo_pa,decimo_termo,razao_pa):
    print (progressao, end = ' ')