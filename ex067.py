while True:
    n = int(input('Digíte um número para ver sua tabuada [negativo para parar]: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO!')