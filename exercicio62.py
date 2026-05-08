#Programa para calcular P.A usando o 'While' de forma melhorada
print ('Calculadora de P.A')
primeiro_termo = int(input('Digite o primeiro termo da P.A: ')) 
razao = int(input('Digite a razão da P.A: '))
termo = primeiro_termo
contador_de_termos = 1
total_de_termos = 0
mais_termos = 10
while mais_termos != 0:
    total_de_termos += mais_termos
    while contador_de_termos <= total_de_termos:
        print(f'{termo} → ', end = '')
        termo += razao
        contador_de_termos += 1
    print('Pausa')
    mais_termos = int(input('\nQuantos termos a mais você quer mostrar? '))
print (f'Fim do programa, você visualizou {total_de_termos} termos da P.A')