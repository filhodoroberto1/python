total = maiormil = menor = cont = 0
barato = ''
print('-' * 40)
print('{:^38}'.format(' LOJA SUPER BARATÃO'))
print('-' * 40)
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço R$'))
    cont += 1
    total += preço
    if preço > 1000:
        maiormil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA  '))
print(f'O total da compra foi R${total:.2f}')
print(f'{maiormil} custam mais que mil reais.')
print(f'O produtoo mais barato foi {barato} que custa R${menor:.2f}')
