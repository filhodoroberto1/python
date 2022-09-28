print('Calcule a soma de todos os números ímpares, que são múltiplos de 3 entre 1 e 500')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
