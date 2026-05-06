#Programa para juntar informações sobre um grupo de pessoas
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
mulheres_menos_20 = 0
for pessoas in range (1,5):
    print('-'*20)
    nome = str(input(f'Digite o {pessoas}° nome: ')).strip()
    idade = int(input(f'Digite a idade da {pessoas} pessoa'))
    sexo = (input(f'Digite o sexo [M/F] da {pessoas} pessoa'))
    soma_idade = soma_idade + idade
    if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome 
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_menos_20 = mulheres_menos_20 + 1
media_idade = soma_idade / 4

print (f'A média de idade das pessoas informadas é igual a; {media_idade}')
print (f'O homem mais velho tem {maior_idade_homem} e se chama {nome_mais_velho}')
print (f'A quantidade de mulheres com menos de 20 anos é igual a: {mulheres_menos_20}')