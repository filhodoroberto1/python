# até 9 mirim, até 14 infantil, até 19 junior, até 25 senior acima master
from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: JUNIOR')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
