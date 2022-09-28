#Faça um programa que leia um número inteiro e mostre seu fatorial.
'''from math import factorial
print('Digite um número para')
n = int(input('calcular seu Fatorial: '))
f = factorial(n)
#print('Calculando {}! = '.format(valor))
print('fatorial de {} é {}'.format(n, f))'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c >0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
