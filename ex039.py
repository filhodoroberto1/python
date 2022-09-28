from datetime import date
atual = date.today().year
nas = int(input('Ano de nascimento: '))
idade = atual - nas
print('Quem nasceu em {}, completa {} anos em {}.'.format(nas, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))
