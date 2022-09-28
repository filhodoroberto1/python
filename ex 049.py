print('Tabuada de uma forma sim  plificada (aula 9)')
n = int(input('Digíte um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
