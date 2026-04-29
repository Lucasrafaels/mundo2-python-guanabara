#Programa para saber se um número é primo ou não
numero = int(input('Digite um número para saber se ele é primo: '))
divisores = 0

for primo in range (1, numero + 1):
    if numero % primo == 0:
        divisores = divisores +1
if divisores == 2:
    condicao = "Primo"
else:
    condicao = 'Não é primo'
    
print(condicao)