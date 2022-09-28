#Desenvolva um program aue leia seis números inteiros e mostre a soma daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite {}º valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} númneros, e a soma é {}'.format(cont, soma))
