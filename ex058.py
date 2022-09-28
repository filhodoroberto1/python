#Melhore o ex 28. Crie um jogo que você tenha que adinhaivar o número qu eo pc pensou. Dando dicas de
#maior ou menor e dizendo no fim em quantas tentativas você acertou.
from random import randint
computador = randint(1, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual fo? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('Acertou com {} tentativas. Parabéns.'.format(palpites))
