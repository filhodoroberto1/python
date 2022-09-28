peso = float(input('Qual é seu peso(kg)? '))
altura = float(input('Qual é sua altura(m)? '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc <= 24.9:
    print('Parabéns, você está no peso normal.')
elif imc <= 25:
    print('Você está com SOBREPESO.')
elif imc <= 30:
    print('Obesidade GRAU UM.')
elif imc <= 35 <= 40:
    print('Obesidade GRAU DOIS.')
elif imca > 40:
    print('Obesidade GRAU TRÊS.')
