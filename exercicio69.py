#Programa para registrar o sexo e a idade de um grupo de pessoas usando o 'while' 
print ('-'*20)
print ('Cadastre uma pessoa')
print ('-'*20)
mais_18_anos = 0
quantidade_homens = 0
mulheres_menos_20 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        sexo = input('Digite o sexo da pessoa[M/F]: ').upper() .strip() [0]
    if idade >= 18:
        mais_18_anos += 1
    if sexo == 'M':
        quantidade_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 +=1
    while continuar not in 'SN':
        continuar = input('Deseja continuar[S/N]? ').upper() .strip() [0]
    if continuar == 'N':
        break

print(f'O total de pessoas com mais de 18 anos é de {mais_18_anos} pessoas, \nA quantidade de homens registradas foi de {quantidade_homens} pessoas \nE o total de mulheres com menos de 20 anos foi de {mulheres_menos_20}')