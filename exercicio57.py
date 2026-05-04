#Programa para registrar o sexo do usuário utilizando o 'while'

sexo = str(input('Digite o seu sexo [M/F]: ')) .upper() .strip()
while sexo not in 'MF':
    sexo = str(input('Dado digitado incorretamente, tente novamente [M/F]: ')) .upper() .strip()
print('O dado foi registrado com suceeso')