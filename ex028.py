#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o úsuario tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
#ou se perdeu.
from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1.5)
if jogador == computador:
    print('OK! Essa você venceu.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
