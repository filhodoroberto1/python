real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/4.32
euro = real/5.13
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar EU{:.2f}'.format(real, euro))