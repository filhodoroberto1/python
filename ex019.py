from random import choice
n1 = str(input('Primeiro(a) aluno(a): '))
n2 = str(input('Segundo(a) aluno(a): '))
n3 = str(input('Terceiro(a) aluno(a): '))
n4 = str(input('Quarto(a) aluno(a): '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O(a) aluno(a) escolhido(a) foi:{} '.format(escolhido))