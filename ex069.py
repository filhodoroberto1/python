tot18 = totmas = totfem = 0
print('_' * 20)
print('CADASTR0 DE PESSOAS')
print('_' * 20)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totmas += 1
    if sexo == 'F' and idade < 20:
        totfem += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totmas} homens cadastrados.')
print(f'Ao todo temos {totfem} com menos de 20 anos.')
