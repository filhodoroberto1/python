#Faça um pro9grama que leia uma frase e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a preimeira vez.
#Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A  primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))