#Desenvolva um programa que poregunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 por km
#para viagens mais longas.

#distância = float(input('Qual é a distância da sua viagem? '))
#print('Você está prestes a começar uma viagem de {:.0f}km.'.format(distância))
#preço = distância * 0.50 if distância <= 200 else distância * 0.45
#print('O preço da sua passagem será de R${:.2f}'.format(preço))      #Maneira simplificada porém mais
                                                                    #desorganizada

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começeçar uma viagem de {:.0f}'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))
