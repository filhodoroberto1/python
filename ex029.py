#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapasasar 80km, mostre uma mensagem dizendo que foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.
velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')