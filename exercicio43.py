'''Programa de cálculo de IMC'''
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
calculo_imc = peso / (altura**2)
if calculo_imc < 18.5:
    print ('O seu IMC está abaixo do peso')
elif calculo_imc < 25:
    print ('O seu IMC está no peso ideal')
elif calculo_imc < 30:
    print ('O seu IMC está como sobrepeso')
elif calculo_imc < 40:
    print ('O seu IMC está como obesidade')
else:
    print ('O seu IMC está como obesidade mórbida')