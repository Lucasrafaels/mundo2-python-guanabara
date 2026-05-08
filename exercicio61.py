#Programa para calcular uma p.a usando 'while'
print ('Calculadora de P.A')
primeiro_termo = int(input('Digite o primeiro termo da P.A: ')) 
razao = int(input('Digite a razão da P.A: '))
#termo = primeiro_termo
contador_de_termos = 1
while contador_de_termos <= 10:
    print(f'{primeiro_termo} → ', end = '')
    primeiro_termo += razao
    contador_de_termos += 1
print ('Fim')