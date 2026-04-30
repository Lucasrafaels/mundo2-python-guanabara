#Exercício para saber se uma frase é um palindromo
frase = str(input('Digite uma frase para saber se ela é um palindromo: ')) .strip() .upper()
palavras = frase.split()
palavras_juntas = '' .join(palavras)
inverso = ''
for letra in range (len(palavras_juntas) - 1,-1,-1):
    inverso = inverso + palavras_juntas[letra]
if inverso ==   palavras_juntas:
    print (f'A sua frase {palavras_juntas} igual a {inverso} por isso ela é um palindromo!')
else:
    print (f'A sua frase {palavras_juntas} igual a {inverso} por isso ela NÃO é um palindromo!')