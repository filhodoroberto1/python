print('Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.\n'
      'Pergunte o valor da casa, o salário, do comprador e em quantos anos ele vai pagar.\n'
      'A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.')
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento:? '))
prestação = casa / (anos * 12)
if prestação >= salário * 30 / 100:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de RS${:.2f}. \n'
          'Empréstimo NEGADO.'.format(casa, anos, prestação))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}. \n'
          'Empréstimo CONCEDIDO.'.format(casa, anos, prestação))
