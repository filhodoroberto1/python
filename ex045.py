from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.3)
print('KEN')
sleep(0.6)
print('PO!!!')
sleep(0.9)
print('-=' * 10)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogada]))
print('-=' * 10)
if computador == 0:
    if jogada == 0:
        print('EMPATE!')
    elif jogada == 1:
        print('VOCÊ VENCEU!')
    elif jogada == 2:
        print('VOCÊ PERDEU!')
    else:
        print('JOGADA INVÁLIDA!!!')
elif computador == 1:
    if jogada == 0:
        print('VOCÊ PERDEU!')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogada == 0:
        print('VOCÊ GANHOU!')
    elif jogada == 1:
        print('VOCÊ PERDEU!')
    elif jogada == 2:
        print('EMPATE!')
