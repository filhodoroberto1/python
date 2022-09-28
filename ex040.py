#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média acima de 7.0: APROVADO
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, média))
if média >= 7.0:
    print('O aluno está APROVADO.')
elif média < 5.0:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está de RECUPERÇÃO')
