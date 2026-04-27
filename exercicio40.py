'''Programa clássico de cálculo de média de notas de um aluno'''
primeira_nota = float(input('Digite a primeira nota do aluno: '))
segunda_nota = float(input('Digite a segunda nota do aluno: '))
media = (primeira_nota + segunda_nota) / 2
if media >= 7:
    print ('Parabéns, o aluno está aprovado!')
elif media >= 5 and media < 7:
    print ('O aluno está de recuperação!')
else:
    print ('O aluno está reprovado!')