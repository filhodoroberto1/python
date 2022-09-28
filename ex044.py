print('========== NELSONS MARKET ==========')
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / PIX
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra será paga em 2x de R${:.2f}'. format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    vezes = int(input('Quantas parcelas? '))
    parcelas = total / vezes
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(vezes, parcelas))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
