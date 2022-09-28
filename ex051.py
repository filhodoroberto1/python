#Desenvolva um programa que leia o primeio termo e a razão de um PA
#No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
num = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = num + (10 - 1) * razão
for c in range(num, décimo + razão, razão):
    print('{} '.format(c), end=' - ')
print('ACABOU')
