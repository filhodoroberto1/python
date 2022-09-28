s = cont = 0
while True:
    n = int(input('Digite um valor [999 para  parar]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} números, e a soma é {s}.')
