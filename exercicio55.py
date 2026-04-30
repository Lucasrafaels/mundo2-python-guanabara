#programa que registra o maior e o menor peso indicado pelo pessoa
maior_peso = 0
menor_peso = 0
for pesos in range (1,6):
    kilos = float(input(f'Digite o {pesos}° peso da pessoa: '))
    if pesos == 1:
        maior_peso = kilos
        menor_peso = kilos
    else:
        if kilos > maior_peso:
            maior_peso = kilos
        if kilos < menor_peso:
            menor_peso = kilos
            
print(f'O maior peso registrado foi o de: {maior_peso}')
print(f'O menor peso registrado foi o de: {menor_peso}')