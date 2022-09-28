#Desenvolva um programa que leia o primeio termo e a razão de um PA
#No final, mostre os 10 primeiros termos dessa progressão, agora usando 'while'. v02
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')