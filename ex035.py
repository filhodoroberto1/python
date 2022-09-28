#Desenvolva um programa que leia o comprimento  de três retas e diga ao usuário se
#elas podem ou não formar um triângulo.
print('-=' * 15)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 15)
a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima {} um triângulo'.format('PODEM FORMAR'))
else:
    print('Os seguimentos acima {} um triângulo'.format('NÃO PODEM FORMAR'))
